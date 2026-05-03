"""
Yusuf Mussa Web UI -- Paymob Payment Gateway Integration.

Supports:
  - Test mode vs Live mode (configurable via settings/env)
  - Authentication token generation
  - Order creation
  - Payment key generation
  - Payment intent creation (card, mobile wallet, kiosk)
  - Webhook handling with HMAC-SHA512 verification
  - Comprehensive error handling with retry logic
  - Transaction status tracking

Paymob API Docs: https://docs.paymob.com/
"""

import hashlib
import hmac
import json
import logging
import os
import time
import threading
import traceback
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

import requests

logger = logging.getLogger(__name__)

# ── Configuration ───────────────────────────────────────────────────────────────

# Paymob API base URLs
TEST_BASE_URL = "https://accept.paymob.com/api"
LIVE_BASE_URL = "https://accept.paymob.com/api"  # Paymob uses same URL; integrations differ by key

# API endpoints
AUTH_ENDPOINT = "/auth/tokens"
ORDER_ENDPOINT = "/ecommerce/orders"
PAYMENT_KEY_ENDPOINT = "/acceptance/payment_keys"
PAYMENT_INTENT_ENDPOINT = "/v1/intention"
CAPTURE_ENDPOINT = "/acceptance/capture"
REFUND_ENDPOINT = "/acceptance/refund"
VOID_ENDPOINT = "/acceptance/void"
TRANSACTION_ENDPOINT = "/acceptance/transactions"

# Paymob integration IDs (test defaults — replace in production)
TEST_CARD_INTEGRATION_ID = os.getenv("PAYMOB_TEST_CARD_INTEGRATION_ID", "4137893")
TEST_WALLET_INTEGRATION_ID = os.getenv("PAYMOB_TEST_WALLET_INTEGRATION_ID", "")
LIVE_CARD_INTEGRATION_ID = os.getenv("PAYMOB_LIVE_CARD_INTEGRATION_ID", "")
LIVE_WALLET_INTEGRATION_ID = os.getenv("PAYMOB_LIVE_WALLET_INTEGRATION_ID", "")

# HMAC secret for webhook verification (from Paymob dashboard)
PAYMOB_HMAC_SECRET = os.getenv("PAYMOB_HMAC_SECRET", "")

# Request timeout (seconds)
REQUEST_TIMEOUT = 30

# Retry configuration
MAX_RETRIES = 3
RETRY_DELAY = 1.0  # seconds, doubles on each retry

# ── In-memory transaction store ────────────────────────────────────────────────
_transactions: dict[str, dict] = {}
_transactions_lock = threading.Lock()

# ── Helper functions ───────────────────────────────────────────────────────────


def _get_config() -> dict:
    """Load Paymob configuration from settings."""
    try:
        from api.config import load_settings
        settings = load_settings()
        return settings.get("paymob", {})
    except Exception:
        return {}


def _is_test_mode() -> bool:
    """Determine if Paymob is in test mode."""
    config = _get_config()
    # Check config first, then env var, default to True (safe default)
    if "test_mode" in config:
        return bool(config["test_mode"])
    return os.getenv("PAYMOB_TEST_MODE", "true").lower() in ("true", "1", "yes")


def _get_api_key() -> str:
    """Get the Paymob API key based on current mode."""
    config = _get_config()
    if _is_test_mode():
        return config.get("test_api_key", "") or os.getenv("PAYMOB_TEST_API_KEY", "")
    return config.get("live_api_key", "") or os.getenv("PAYMOB_LIVE_API_KEY", "")


def _get_base_url() -> str:
    """Get the base URL for Paymob API calls."""
    return TEST_BASE_URL if _is_test_mode() else LIVE_BASE_URL


def _get_card_integration_id() -> str:
    """Get the card integration ID based on current mode."""
    if _is_test_mode():
        return TEST_CARD_INTEGRATION_ID
    return LIVE_CARD_INTEGRATION_ID or TEST_CARD_INTEGRATION_ID


def _get_wallet_integration_id() -> str:
    """Get the mobile wallet integration ID based on current mode."""
    if _is_test_mode():
        return TEST_WALLET_INTEGRATION_ID
    return LIVE_WALLET_INTEGRATION_ID or TEST_WALLET_INTEGRATION_ID


# ── Custom Exceptions ──────────────────────────────────────────────────────────


class PaymobError(Exception):
    """Base exception for Paymob errors."""
    def __init__(self, message: str, code: str = "PAYMOB_ERROR", status_code: int = 500, detail: Any = None):
        super().__init__(message)
        self.code = code
        self.status_code = status_code
        self.detail = detail


class PaymobAuthError(PaymobError):
    """Authentication token generation failed."""
    def __init__(self, message: str = "Paymob authentication failed", detail: Any = None):
        super().__init__(message, code="PAYMOB_AUTH_ERROR", status_code=401, detail=detail)


class PaymobOrderError(PaymobError):
    """Order creation/management failed."""
    def __init__(self, message: str = "Paymob order operation failed", detail: Any = None):
        super().__init__(message, code="PAYMOB_ORDER_ERROR", status_code=400, detail=detail)


class PaymobPaymentError(PaymobError):
    """Payment key/intent generation failed."""
    def __init__(self, message: str = "Paymob payment operation failed", detail: Any = None):
        super().__init__(message, code="PAYMOB_PAYMENT_ERROR", status_code=400, detail=detail)


class PaymobWebhookError(PaymobError):
    """Webhook verification failed."""
    def __init__(self, message: str = "Paymob webhook verification failed", detail: Any = None):
        super().__init__(message, code="PAYMOB_WEBHOOK_ERROR", status_code=400, detail=detail)


class PaymobConfigError(PaymobError):
    """Configuration error (missing API key, etc.)."""
    def __init__(self, message: str = "Paymob configuration error", detail: Any = None):
        super().__init__(message, code="PAYMOB_CONFIG_ERROR", status_code=500, detail=detail)


# ── API Communication with Retry ───────────────────────────────────────────────


def _make_request(method: str, endpoint: str, payload: dict = None, headers: dict = None) -> dict:
    """Make an HTTP request to the Paymob API with retry logic.

    Args:
        method: HTTP method ("POST", "GET", etc.)
        endpoint: API endpoint path (e.g., "/auth/tokens")
        payload: Request body as dict
        headers: Additional headers

    Returns:
        Response body as dict

    Raises:
        PaymobError: On request failure after retries
    """
    base_url = _get_base_url()
    url = f"{base_url}{endpoint}"

    default_headers = {"Content-Type": "application/json"}
    if headers:
        default_headers.update(headers)

    last_error = None
    for attempt in range(MAX_RETRIES):
        try:
            if method.upper() == "POST":
                resp = requests.post(
                    url,
                    json=payload,
                    headers=default_headers,
                    timeout=REQUEST_TIMEOUT,
                )
            elif method.upper() == "GET":
                resp = requests.get(
                    url,
                    headers=default_headers,
                    timeout=REQUEST_TIMEOUT,
                )
            else:
                raise PaymobError(f"Unsupported HTTP method: {method}")

            # Check for HTTP errors
            if resp.status_code >= 500:
                # Server error — retry
                last_error = PaymobError(
                    f"Paymob server error (HTTP {resp.status_code})",
                    code="PAYMOB_SERVER_ERROR",
                    status_code=resp.status_code,
                    detail=resp.text[:500],
                )
                if attempt < MAX_RETRIES - 1:
                    delay = RETRY_DELAY * (2 ** attempt)
                    logger.warning(
                        "Paymob request failed (attempt %d/%d), retrying in %.1fs: %s",
                        attempt + 1, MAX_RETRIES, delay, resp.status_code,
                    )
                    time.sleep(delay)
                    continue
                raise last_error

            if resp.status_code >= 400:
                # Client error — don't retry
                try:
                    error_detail = resp.json()
                except Exception:
                    error_detail = resp.text[:500]

                error_msg = (
                    error_detail.get("detail", "")
                    if isinstance(error_detail, dict)
                    else str(error_detail)
                )

                if resp.status_code == 401:
                    raise PaymobAuthError(
                        f"Authentication failed: {error_msg}",
                        detail=error_detail,
                    )
                elif "order" in endpoint.lower():
                    raise PaymobOrderError(
                        f"Order operation failed: {error_msg}",
                        detail=error_detail,
                    )
                elif "payment" in endpoint.lower() or "intention" in endpoint.lower():
                    raise PaymobPaymentError(
                        f"Payment operation failed: {error_msg}",
                        detail=error_detail,
                    )
                else:
                    raise PaymobError(
                        f"Paymob API error (HTTP {resp.status_code}): {error_msg}",
                        status_code=resp.status_code,
                        detail=error_detail,
                    )

            # Success
            try:
                return resp.json()
            except Exception:
                return {"raw_response": resp.text}

        except requests.Timeout:
            last_error = PaymobError(
                "Paymob request timed out",
                code="PAYMOB_TIMEOUT",
                status_code=504,
            )
            if attempt < MAX_RETRIES - 1:
                delay = RETRY_DELAY * (2 ** attempt)
                logger.warning(
                    "Paymob request timed out (attempt %d/%d), retrying in %.1fs",
                    attempt + 1, MAX_RETRIES, delay,
                )
                time.sleep(delay)
                continue

        except requests.ConnectionError:
            last_error = PaymobError(
                "Failed to connect to Paymob API",
                code="PAYMOB_CONNECTION_ERROR",
                status_code=502,
            )
            if attempt < MAX_RETRIES - 1:
                delay = RETRY_DELAY * (2 ** attempt)
                logger.warning(
                    "Paymob connection error (attempt %d/%d), retrying in %.1fs",
                    attempt + 1, MAX_RETRIES, delay,
                )
                time.sleep(delay)
                continue

        except PaymobError:
            raise

        except Exception as e:
            last_error = PaymobError(
                f"Unexpected error: {e}",
                code="PAYMOB_UNEXPECTED_ERROR",
            )

    raise last_error or PaymobError("Max retries exceeded")


# ── Authentication ─────────────────────────────────────────────────────────────


def authenticate() -> str:
    """Generate an authentication token from Paymob API.

    Returns:
        Authentication token string

    Raises:
        PaymobAuthError: If authentication fails
        PaymobConfigError: If API key is not configured
    """
    api_key = _get_api_key()
    if not api_key:
        raise PaymobConfigError(
            "Paymob API key is not configured. Set PAYMOB_TEST_API_KEY or PAYMOB_LIVE_API_KEY environment variable, "
            "or configure it in Settings.",
        )

    payload = {"api_key": api_key}
    response = _make_request("POST", AUTH_ENDPOINT, payload=payload)

    token = response.get("token")
    if not token:
        raise PaymobAuthError(
            "No token in Paymob auth response",
            detail=response,
        )

    logger.info("Paymob authentication successful (test_mode=%s)", _is_test_mode())
    return token


# ── Order Management ───────────────────────────────────────────────────────────


def create_order(
    amount_cents: int,
    currency: str = "EGP",
    merchant_order_id: str = None,
    items: list = None,
    delivery_needed: bool = False,
    shipping_data: dict = None,
    metadata: dict = None,
) -> dict:
    """Create a new order in Paymob.

    Args:
        amount_cents: Amount in cents (e.g., 10000 = 100.00 EGP)
        currency: Currency code (default: EGP)
        merchant_order_id: Custom order ID (auto-generated if not provided)
        items: List of order items
        delivery_needed: Whether delivery is needed
        shipping_data: Shipping information
        metadata: Custom metadata to attach to the order

    Returns:
        Order creation response from Paymob

    Raises:
        PaymobOrderError: If order creation fails
    """
    token = authenticate()

    if not merchant_order_id:
        merchant_order_id = f"YM-{int(time.time())}-{uuid.uuid4().hex[:8]}"

    payload = {
        "auth_token": token,
        "delivery_needed": delivery_needed,
        "merchant_order_id": merchant_order_id,
        "amount_cents": amount_cents,
        "currency": currency,
    }

    if items:
        payload["items"] = items

    if shipping_data:
        payload["shipping_data"] = shipping_data

    if metadata:
        payload["extras"] = metadata

    response = _make_request("POST", ORDER_ENDPOINT, payload=payload)

    # Store transaction locally
    order_id = str(response.get("id", ""))
    with _transactions_lock:
        _transactions[merchant_order_id] = {
            "merchant_order_id": merchant_order_id,
            "paymob_order_id": order_id,
            "amount_cents": amount_cents,
            "currency": currency,
            "status": "created",
            "created_at": datetime.now(timezone.utc).isoformat(),
            "test_mode": _is_test_mode(),
            "items": items or [],
            "metadata": metadata or {},
        }

    logger.info(
        "Paymob order created: merchant_order_id=%s paymob_order_id=%s amount=%d cents",
        merchant_order_id, order_id, amount_cents,
    )
    return response


# ── Payment Key Generation ────────────────────────────────────────────────────


def generate_payment_key(
    order_id: str | int,
    amount_cents: int,
    billing_data: dict,
    currency: str = "EGP",
    integration_id: str = None,
    expiration: int = 3600,
) -> dict:
    """Generate a payment key for a specific order.

    Args:
        order_id: Paymob order ID (from create_order response)
        amount_cents: Amount in cents
        billing_data: Customer billing info (first_name, last_name, email, phone_number required)
        currency: Currency code
        integration_id: Paymob integration ID (auto-selected if not provided)
        expiration: Payment key expiration in seconds (default: 3600 = 1 hour)

    Returns:
        Payment key response from Paymob (contains 'token' field)

    Raises:
        PaymobPaymentError: If payment key generation fails
    """
    token = authenticate()

    if not integration_id:
        integration_id = _get_card_integration_id()

    # Validate required billing data fields
    required_fields = ["first_name", "last_name", "email", "phone_number"]
    missing = [f for f in required_fields if not billing_data.get(f)]
    if missing:
        raise PaymobPaymentError(
            f"Missing required billing data fields: {', '.join(missing)}",
            detail={"missing_fields": missing},
        )

    # Set defaults for optional billing fields
    billing_defaults = {
        "apartment": "NA",
        "floor": "NA",
        "street": "NA",
        "building": "NA",
        "shipping_method": "NA",
        "postal_code": "NA",
        "city": "NA",
        "country": "EG",
        "state": "NA",
    }
    for key, default in billing_defaults.items():
        billing_data.setdefault(key, default)

    payload = {
        "auth_token": token,
        "amount_cents": amount_cents,
        "expiration": expiration,
        "order_id": str(order_id),
        "billing_data": billing_data,
        "currency": currency,
        "integration_id": int(integration_id),
    }

    response = _make_request("POST", PAYMENT_KEY_ENDPOINT, payload=payload)

    logger.info(
        "Paymob payment key generated: order_id=%s integration_id=%s",
        order_id, integration_id,
    )
    return response


# ── Payment Intent (New Paymob API) ───────────────────────────────────────────


def create_payment_intent(
    amount_cents: int,
    currency: str = "EGP",
    payment_methods: list = None,
    items: list = None,
    billing_data: dict = None,
    delivery_needed: bool = False,
    shipping_data: dict = None,
    merchant_order_id: str = None,
    extras: dict = None,
    special_fees: list = None,
) -> dict:
    """Create a payment intention using Paymob's v1/intention API.

    This is the recommended way to create payments with Paymob's newer API.
    It returns a client_secret that can be used with the Paymob JS SDK.

    Args:
        amount_cents: Amount in cents
        currency: Currency code
        payment_methods: List of payment method config dicts
            [{"type": "card"}, {"type": "wallet", "mobile_number": "01012345678"}]
        items: Order items
        billing_data: Customer billing info
        delivery_needed: Whether delivery is needed
        shipping_data: Shipping data
        merchant_order_id: Custom order ID
        extras: Custom metadata
        special_fees: Special fees configuration

    Returns:
        Payment intent response (contains client_secret)

    Raises:
        PaymobPaymentError: If intent creation fails
    """
    api_key = _get_api_key()
    if not api_key:
        raise PaymobConfigError("Paymob API key not configured")

    if not merchant_order_id:
        merchant_order_id = f"YM-{int(time.time())}-{uuid.uuid4().hex[:8]}"

    if not payment_methods:
        integration_id = _get_card_integration_id()
        payment_methods = [{"type": "card", "integration_id": int(integration_id)}]

    payload = {
        "amount": amount_cents,
        "currency": currency,
        "payment_methods": payment_methods,
        "merchant_order_id": merchant_order_id,
    }

    if items:
        payload["items"] = items
    if billing_data:
        payload["billing_data"] = billing_data
    if delivery_needed:
        payload["delivery_needed"] = delivery_needed
    if shipping_data:
        payload["shipping_data"] = shipping_data
    if extras:
        payload["extras"] = extras
    if special_fees:
        payload["special_fees"] = special_fees

    # The v1/intention endpoint uses the API key in the Authorization header
    headers = {"Authorization": f"Token {api_key}"}
    response = _make_request("POST", PAYMENT_INTENT_ENDPOINT, payload=payload, headers=headers)

    # Store transaction locally
    with _transactions_lock:
        _transactions[merchant_order_id] = {
            "merchant_order_id": merchant_order_id,
            "paymob_order_id": str(response.get("id", "")),
            "client_secret": response.get("client_secret", ""),
            "amount_cents": amount_cents,
            "currency": currency,
            "status": "intent_created",
            "created_at": datetime.now(timezone.utc).isoformat(),
            "test_mode": _is_test_mode(),
            "payment_methods": payment_methods,
            "extras": extras or {},
        }

    logger.info(
        "Paymob payment intent created: merchant_order_id=%s amount=%d cents",
        merchant_order_id, amount_cents,
    )
    return response


# ── Webhook Handling ───────────────────────────────────────────────────────────

# Paymob webhook HMAC fields (ordered as per Paymob docs)
_HMAC_TRANSACTION_FIELDS = [
    "amount_cents",
    "created_at",
    "currency",
    "error_occured",
    "has_parent_transaction",
    "id",
    "integration_id",
    "is_3d_secure",
    "is_auth",
    "is_capture",
    "is_refunded",
    "is_standalone_payment",
    "is_voided",
    "order.id",
    "owner",
    "pending",
    "source_data.pan",
    "source_data.sub_type",
    "source_data.type",
    "success",
]

_HMAC_RESPONSE_FIELDS = [
    "amount_cents",
    "created_at",
    "currency",
    "error_occured",
    "has_parent_transaction",
    "id",
    "integration_id",
    "is_3d_secure",
    "is_auth",
    "is_capture",
    "is_refunded",
    "is_standalone_payment",
    "is_voided",
    "order",
    "owner",
    "pending",
    "source_data.pan",
    "source_data.sub_type",
    "source_data.type",
    "success",
]


def _extract_nested_value(data: dict, key: str) -> str:
    """Extract a value from a nested dict using dot notation.

    E.g., _extract_nested_value(data, "order.id") returns data["order"]["id"]
    """
    parts = key.split(".")
    current = data
    for part in parts:
        if isinstance(current, dict):
            current = current.get(part, "")
        else:
            return ""
    return str(current) if current is not None else ""


def verify_webhook_hmac(data: dict, hmac_header: str) -> bool:
    """Verify the HMAC signature of a Paymob webhook.

    Paymob signs webhook payloads with HMAC-SHA512 using a shared secret.
    This function reconstructs the signature from the payload and compares it.

    Args:
        data: Webhook payload dict (the "obj" field)
        hmac_header: The HMAC value from the webhook headers or query string

    Returns:
        True if the HMAC is valid, False otherwise
    """
    secret = PAYMOB_HMAC_SECRET or _get_config().get("hmac_secret", "")
    if not secret:
        logger.warning("Paymob HMAC secret not configured — skipping webhook verification")
        return True  # If no secret configured, skip verification (not recommended for production)

    if not hmac_header:
        logger.warning("No HMAC header provided in webhook")
        return False

    # Build the concatenated string from the transaction fields
    # Try both field sets (Paymob uses different field sets depending on the webhook type)
    for field_set in (_HMAC_RESPONSE_FIELDS, _HMAC_TRANSACTION_FIELDS):
        values = []
        for field in field_set:
            val = _extract_nested_value(data, field)
            values.append(val)

        concatenated = "".join(values)

        # Compute HMAC-SHA512
        computed = hmac.new(
            secret.encode("utf-8"),
            concatenated.encode("utf-8"),
            hashlib.sha512,
        ).hexdigest()

        if hmac.compare_digest(computed, hmac_header):
            return True

    logger.warning("Paymob webhook HMAC verification failed")
    return False


def handle_webhook(payload: dict, hmac_header: str = None) -> dict:
    """Process a Paymob webhook notification.

    This is the main entry point for webhook handling. It:
    1. Verifies the HMAC signature
    2. Extracts transaction details
    3. Updates the local transaction store
    4. Returns a structured result

    Args:
        payload: The full webhook payload
        hmac_header: HMAC value from headers (e.g., "hmac" query param or "X-Paymob-Hmac" header)

    Returns:
        Processing result dict with status and details

    Raises:
        PaymobWebhookError: If HMAC verification fails
    """
    if not isinstance(payload, dict):
        raise PaymobWebhookError("Invalid webhook payload: expected dict")

    # Paymob webhooks have the transaction data in "obj" field
    transaction_data = payload.get("obj", payload)

    # Verify HMAC if header is provided
    if hmac_header:
        if not verify_webhook_hmac(transaction_data, hmac_header):
            raise PaymobWebhookError(
                "HMAC verification failed — webhook may be tampered",
                detail={"hmac_provided": hmac_header[:16] + "..."},
            )

    # Extract key transaction fields
    transaction_id = str(transaction_data.get("id", ""))
    order_data = transaction_data.get("order", {})
    order_id = str(order_data.get("id", "")) if isinstance(order_data, dict) else str(order_data)
    merchant_order_id = order_data.get("merchant_order_id", "") if isinstance(order_data, dict) else ""

    success = transaction_data.get("success", False)
    pending = transaction_data.get("pending", False)
    is_voided = transaction_data.get("is_voided", False)
    is_refunded = transaction_data.get("is_refunded", False)
    is_capture = transaction_data.get("is_capture", False)
    is_auth = transaction_data.get("is_auth", False)
    error_occured = transaction_data.get("error_occured", False)
    amount_cents = transaction_data.get("amount_cents", 0)
    currency = transaction_data.get("currency", "EGP")

    # Determine status
    if is_voided:
        status = "voided"
    elif is_refunded:
        status = "refunded"
    elif success and not pending:
        status = "successful"
    elif pending:
        status = "pending"
    elif error_occured:
        status = "failed"
    else:
        status = "unknown"

    # Get error details if any
    error_detail = None
    if error_occured:
        error_detail = transaction_data.get("data", {}).get("message", "") if isinstance(transaction_data.get("data"), dict) else str(transaction_data.get("data", ""))

    # Update local transaction store
    with _transactions_lock:
        # Try to find existing transaction by merchant_order_id or paymob_order_id
        existing = None
        if merchant_order_id and merchant_order_id in _transactions:
            existing = _transactions[merchant_order_id]
        else:
            for tx in _transactions.values():
                if tx.get("paymob_order_id") == order_id:
                    existing = tx
                    break

        if existing:
            existing["status"] = status
            existing["paymob_transaction_id"] = transaction_id
            existing["updated_at"] = datetime.now(timezone.utc).isoformat()
            if error_detail:
                existing["error"] = error_detail
        else:
            # Store as new entry
            key = merchant_order_id or f"paymob-{transaction_id}"
            _transactions[key] = {
                "merchant_order_id": merchant_order_id,
                "paymob_order_id": order_id,
                "paymob_transaction_id": transaction_id,
                "amount_cents": amount_cents,
                "currency": currency,
                "status": status,
                "success": success,
                "pending": pending,
                "is_voided": is_voided,
                "is_refunded": is_refunded,
                "is_capture": is_capture,
                "is_auth": is_auth,
                "error": error_detail,
                "created_at": datetime.now(timezone.utc).isoformat(),
                "updated_at": datetime.now(timezone.utc).isoformat(),
                "test_mode": _is_test_mode(),
            }

    result = {
        "processed": True,
        "transaction_id": transaction_id,
        "order_id": order_id,
        "merchant_order_id": merchant_order_id,
        "status": status,
        "amount_cents": amount_cents,
        "currency": currency,
        "success": success,
        "pending": pending,
        "error": error_detail,
    }

    logger.info(
        "Paymob webhook processed: tx_id=%s order_id=%s status=%s amount=%d",
        transaction_id, order_id, status, amount_cents,
    )

    return result


# ── Transaction Operations ─────────────────────────────────────────────────────


def capture_transaction(transaction_id: str, amount_cents: int = None) -> dict:
    """Capture a previously authorized transaction.

    Args:
        transaction_id: Paymob transaction ID
        amount_cents: Amount to capture (defaults to full auth amount)

    Returns:
        Capture response from Paymob
    """
    token = authenticate()
    payload = {"auth_token": token, "transaction_id": int(transaction_id)}
    if amount_cents:
        payload["amount_cents"] = amount_cents

    response = _make_request("POST", CAPTURE_ENDPOINT, payload=payload)
    logger.info("Paymob transaction captured: tx_id=%s", transaction_id)
    return response


def refund_transaction(transaction_id: str, amount_cents: int = None) -> dict:
    """Refund a transaction.

    Args:
        transaction_id: Paymob transaction ID
        amount_cents: Amount to refund (defaults to full amount)

    Returns:
        Refund response from Paymob
    """
    token = authenticate()
    payload = {"auth_token": token, "transaction_id": int(transaction_id)}
    if amount_cents:
        payload["amount_cents"] = amount_cents

    response = _make_request("POST", REFUND_ENDPOINT, payload=payload)
    logger.info("Paymob transaction refunded: tx_id=%s", transaction_id)
    return response


def void_transaction(transaction_id: str) -> dict:
    """Void a transaction.

    Args:
        transaction_id: Paymob transaction ID

    Returns:
        Void response from Paymob
    """
    token = authenticate()
    payload = {"auth_token": token, "transaction_id": int(transaction_id)}

    response = _make_request("POST", VOID_ENDPOINT, payload=payload)
    logger.info("Paymob transaction voided: tx_id=%s", transaction_id)
    return response


def get_transaction(transaction_id: str) -> dict:
    """Retrieve transaction details from Paymob.

    Args:
        transaction_id: Paymob transaction ID

    Returns:
        Transaction details from Paymob
    """
    token = authenticate()
    headers = {"Authorization": f"Bearer {token}"}

    endpoint = f"{TRANSACTION_ENDPOINT}/{transaction_id}"
    response = _make_request("GET", endpoint, headers=headers)
    return response


# ── Local Transaction Store ────────────────────────────────────────────────────


def list_transactions(limit: int = 50, offset: int = 0) -> list[dict]:
    """List locally stored transactions.

    Args:
        limit: Maximum number of transactions to return
        offset: Offset for pagination

    Returns:
        List of transaction dicts
    """
    with _transactions_lock:
        all_txs = list(_transactions.values())

    # Sort by created_at descending
    all_txs.sort(key=lambda x: x.get("created_at", ""), reverse=True)

    return all_txs[offset:offset + limit]


def get_local_transaction(merchant_order_id: str) -> Optional[dict]:
    """Get a locally stored transaction by merchant_order_id.

    Args:
        merchant_order_id: The merchant order ID

    Returns:
        Transaction dict or None if not found
    """
    with _transactions_lock:
        return _transactions.get(merchant_order_id)


# ── Configuration Status ───────────────────────────────────────────────────────


def get_paymob_status() -> dict:
    """Get the current Paymob configuration status.

    Returns:
        Status dict with configuration details (sensitive data redacted)
    """
    api_key = _get_api_key()
    test_mode = _is_test_mode()

    return {
        "configured": bool(api_key),
        "test_mode": test_mode,
        "mode": "test" if test_mode else "live",
        "card_integration_id": _get_card_integration_id() or "not configured",
        "wallet_integration_id": _get_wallet_integration_id() or "not configured",
        "hmac_configured": bool(PAYMOB_HMAC_SECRET or _get_config().get("hmac_secret")),
        "api_key_set": bool(api_key),
        "api_key_preview": f"{'*' * 8}{api_key[-4:]}" if api_key and len(api_key) > 4 else "not set",
    }


# ── Utility: Generate Paymob Iframe URL ────────────────────────────────────────


def get_payment_iframe_url(payment_key_token: str, iframe_id: str = None) -> str:
    """Generate a Paymob iframe payment URL.

    Args:
        payment_key_token: The payment key token from generate_payment_key
        iframe_id: Paymob iframe ID (from settings or env)

    Returns:
        Full iframe URL for redirecting the user
    """
    config = _get_config()
    if not iframe_id:
        iframe_id = config.get("iframe_id", "") or os.getenv("PAYMOB_IFRAME_ID", "")

    if not iframe_id:
        raise PaymobConfigError("Paymob iframe ID not configured")

    base_url = _get_base_url()
    return f"{base_url}/acceptance/iframes/{iframe_id}?payment_token={payment_key_token}"
