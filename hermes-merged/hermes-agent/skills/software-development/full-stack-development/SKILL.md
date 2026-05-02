---
name: full-stack-development
description: "Build full-stack web applications, SaaS products, and complex software systems end-to-end — from database schema to deployed production service."
version: 2.0.0
author: Yusuf Mussa Agent Enhancement
category: software-development
tags: [full-stack, saas, web, api, database, devops, mobile, ui-ux, architecture, debugging]
tools: [terminal, file, web, browser, code_execution, delegation, memory, todo, cronjob, image_gen]
metadata:
  hermes:
    tags: [full-stack, saas, web-development, api, database, devops, mobile, debugging, code-review, ui-ux]
    related_skills: [subagent-driven-development, systematic-debugging, test-driven-development, writing-plans, requesting-code-review, browser-automation, yusuf-mussa-tools]
---

# Full-Stack Development

## Overview

End-to-end software development capability — from ideation to production deployment. Build complete web applications, SaaS products, mobile apps, APIs, and distributed systems. This skill covers the entire software development lifecycle with emphasis on production quality, security, and scalability.

**Core principle:** Ship production-ready software. Every feature includes tests, error handling, security hardening, and documentation.

## Capabilities

### 1. Full-Stack Web Applications

Build complete web applications with modern frameworks:

**Frontend:**
- Next.js 14+ (App Router, Server Components, Server Actions)
- React 18+ with hooks, context, suspense
- Vue 3 with Composition API and Nuxt
- SvelteKit for performance-critical apps
- Tailwind CSS 4, shadcn/ui, Radix UI for design systems
- TypeScript for type safety across the stack

**Backend:**
- Python: Django, Flask, FastAPI, Starlette
- Node.js: Express, Fastify, Hono, tRPC
- Rust: Actix-web, Axum
- Go: Gin, Echo, Fiber

**Pattern:**
```
1. Scaffold project with chosen framework
2. Define database schema and models
3. Build API layer (REST or GraphQL)
4. Implement business logic with tests
5. Build frontend components with responsive design
6. Add authentication and authorization
7. Write end-to-end tests
8. Deploy to production
```

### 2. SaaS Product Engineering

Build multi-tenant SaaS products with complete business infrastructure:

**Authentication & Authorization:**
- NextAuth.js / Clerk / Auth0 / Supabase Auth
- JWT, OAuth 2.0, SSO, MFA
- Role-based access control (RBAC)
- Team/organization management

**Billing & Payments:**
- Stripe integration (subscriptions, one-time, usage-based)
- Lemon Squeezy, Paddle for merchant-of-record
- Webhook handling for payment events
- Usage metering and quota enforcement

**Multi-Tenancy:**
- Schema-per-tenant vs row-level isolation
- Tenant context middleware
- Per-tenant configuration and feature flags
- Data migration strategies

**Email & Notifications:**
- SendGrid, Resend, AWS SES for transactional email
- Push notifications (web, mobile)
- In-app notification systems
- Email templates with React Email / MJML

### 3. Mobile App Development

**Cross-Platform:**
- React Native with Expo for rapid development
- Flutter for performance-sensitive apps
- Progressive Web Apps (PWA) for web-first mobile

**Native Integrations:**
- Camera, GPS, biometrics, push notifications
- App Store and Play Store deployment
- Deep linking and app shortcuts

### 4. Database Design & Management

**Relational (PostgreSQL, MySQL, SQLite):**
- Normalized schema design with proper indexing
- Migration management with Alembic, Prisma, Drizzle
- Query optimization and EXPLAIN analysis
- Connection pooling (PgBouncer, Prisma)

**NoSQL (MongoDB, Redis, DynamoDB):**
- Document modeling and embedding strategies
- Caching layers with Redis
- Time-series data with InfluxDB/TimescaleDB

**ORM/Query Builders:**
- Prisma (TypeScript), SQLAlchemy (Python), Drizzle (TypeScript)
- GORM (Go), Diesel (Rust)

### 5. API Design & Implementation

**REST APIs:**
- OpenAPI/Swagger specification
- Resource-oriented design with proper HTTP semantics
- Pagination, filtering, sorting patterns
- Rate limiting and request throttling
- Versioning strategies

**GraphQL:**
- Schema design with Apollo Server / Yoga
- DataLoader for N+1 prevention
- Subscription support for real-time updates

**Real-Time:**
- WebSocket with Socket.io / FastAPI WebSocket
- Server-Sent Events (SSE)
- Webhook design patterns

### 6. DevOps & Deployment

**Containerization:**
- Docker multi-stage builds for optimized images
- Docker Compose for local development
- Container orchestration basics

**CI/CD:**
- GitHub Actions workflows
- Automated testing, linting, and deployment
- Preview deployments for PRs (Vercel, Netlify)

**Cloud Deployment:**
- Vercel / Netlify for frontend and serverless
- Railway / Render / Fly.io for full-stack
- AWS (EC2, Lambda, S3, RDS) / GCP / Azure
- Infrastructure as Code (Terraform, Pulumi)

**Monitoring:**
- Application logging (structured JSON logs)
- Error tracking (Sentry)
- Performance monitoring (APM)
- Health checks and alerting

### 7. Debugging & Error Fixing

**Systematic Approach:**
1. Reproduce the error reliably
2. Identify the scope (frontend, backend, database, network)
3. Read error messages and stack traces carefully
4. Check logs for related errors
5. Isolate the root cause with minimal reproduction
6. Write a failing test that demonstrates the bug
7. Fix the bug
8. Verify the test passes
9. Run full test suite for regressions
10. Document the fix

**Common Debugging Tools:**
- `terminal` for running debuggers (pdb, node --inspect, rust-gdb)
- `read_file` / `search_files` for code investigation
- `execute_code` for isolated reproduction
- `browser_navigate` / `browser_snapshot` for UI debugging
- `web_search` for researching error messages

### 8. Code Review & Optimization

**Review Checklist:**
- [ ] Code correctness and edge case handling
- [ ] Security vulnerabilities (injection, XSS, CSRF, auth bypass)
- [ ] Performance (N+1 queries, memory leaks, unnecessary re-renders)
- [ ] Error handling completeness
- [ ] Test coverage adequacy
- [ ] API contract compliance
- [ ] Documentation accuracy
- [ ] Naming clarity and code organization

**Optimization Strategies:**
- Database query optimization (indexing, query plans)
- Caching strategies (Redis, CDN, browser cache)
- Bundle size reduction (tree-shaking, code splitting)
- Image optimization (WebP, lazy loading, responsive images)
- API response compression and pagination

### 9. UI/UX Design & Implementation

**Design Principles:**
- Mobile-first responsive design
- Accessibility (WCAG 2.1 AA compliance)
- Consistent design system (colors, typography, spacing)
- Progressive enhancement
- Performance budgets (Core Web Vitals)

**Implementation:**
- Tailwind CSS for utility-first styling
- shadcn/ui for accessible component primitives
- Framer Motion for animations
- Dark mode with system preference detection
- RTL support for Arabic and other RTL languages

**Design Tooling:**
- `image_generate` for mockups and visual assets
- `browser_navigate` / `browser_snapshot` for visual testing
- HTML/CSS for rapid prototyping

## Workflow Templates

### New SaaS Project

```
1. Create project plan with writing-plans skill
2. Set up project scaffold (framework, linting, CI)
3. Design and implement database schema
4. Build authentication system
5. Implement core API endpoints with tests
6. Build frontend pages and components
7. Add billing integration
8. Set up deployment pipeline
9. Run security audit
10. Deploy to production
```

### Bug Fix Workflow

```
1. Load systematic-debugging skill
2. Reproduce the issue
3. Write failing test
4. Fix root cause
5. Verify all tests pass
6. Deploy fix
```

### Feature Addition

```
1. Load writing-plans skill for design
2. Create implementation plan
3. Load subagent-driven-development skill
4. Execute plan with subagents
5. Load requesting-code-review skill
6. Review and merge
```

## Technology Decision Matrix

| Scenario | Frontend | Backend | Database | Deployment |
|---|---|---|---|---|
| SaaS MVP | Next.js + shadcn/ui | Next.js API Routes | PostgreSQL + Prisma | Vercel |
| API Service | - | FastAPI + Pydantic | PostgreSQL + SQLAlchemy | Railway / Fly.io |
| Real-time App | React + Socket.io | FastAPI WebSocket | Redis + PostgreSQL | AWS / GCP |
| Content Site | Next.js SSG | - | SQLite / MDX files | Vercel / Netlify |
| Mobile App | React Native + Expo | FastAPI / Django | PostgreSQL | AWS / Firebase |
| Microservices | React | Go + Gin / Rust + Axum | PostgreSQL + Redis | Kubernetes |

## Security Checklist

Every project must address:

- [ ] Input validation and sanitization on all endpoints
- [ ] SQL injection prevention (parameterized queries / ORM)
- [ ] XSS prevention (CSP headers, output encoding)
- [ ] CSRF protection for state-changing requests
- [ ] Authentication with secure session/token management
- [ ] Authorization checks on every protected route
- [ ] Rate limiting on API endpoints
- [ ] HTTPS everywhere (HSTS headers)
- [ ] Secrets management (env vars, not hardcoded)
- [ ] Dependency audit for known vulnerabilities
- [ ] CORS configuration
- [ ] File upload validation and size limits

## Integration with Other Skills

- **`writing-plans`**: Create implementation plans before building
- **`subagent-driven-development`**: Execute plans with subagents for parallel work
- **`systematic-debugging`**: Debug complex issues methodically
- **`test-driven-development`**: Write tests first, implement second
- **`requesting-code-review`**: Get thorough code reviews
- **`browser-automation`**: Test and debug web UIs
- **`yusuf-mussa-tools`**: Reference for trending AI integrations

## Remember

```
Ship production-ready code
Every feature includes tests
Security is not optional
Design for scale from the start
Document as you build
Debug systematically, fix root causes
Review code before merging
Deploy with confidence
```

**Build software that works, scales, and lasts.**
