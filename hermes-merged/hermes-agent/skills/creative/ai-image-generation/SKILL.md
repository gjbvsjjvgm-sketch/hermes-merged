---
name: ai-image-generation
version: 1.0.0
description: Multi-provider AI image generation - DALL-E 3, Flux, Stable Diffusion, Midjourney, and ComfyUI workflows
category: creative
tags: [image, generation, dall-e, flux, stable-diffusion, art, creative]
tools: [terminal, file]
---

# AI Image Generation

Create images using multiple AI generation providers - from quick sketches to production artwork.

## Supported Providers

| Provider | Quality | Speed | Style Range | Cost |
|----------|---------|-------|-------------|------|
| DALL-E 3 | Excellent | Fast | Wide | Per-image |
| Flux (Replicate) | Excellent | Medium | Wide | Pay-per-use |
| Stable Diffusion | Good | Varies | Customizable | Free (local) |
| ComfyUI | Excellent | Varies | Unlimited | Free (local) |
| Midjourney | Excellent | Medium | Artistic | Subscription |

## Usage Examples

User: "Generate an image of a sunset over mountains"
→ Use configured image generation provider to create the image

User: "Create a logo for my startup"
→ Generate multiple logo variations with different styles

User: "Edit this image to add a blue sky"
→ Use DALL-E edit API or inpainting with Stable Diffusion

User: "Generate images in bulk with different styles"
→ Use ComfyUI batch workflow

## Prompt Engineering Tips
1. Be specific about style, lighting, composition
2. Include technical details (8K, photorealistic, etc.)
3. Reference art styles or artists for direction
4. Specify aspect ratio and format
5. Use negative prompts to exclude unwanted elements
