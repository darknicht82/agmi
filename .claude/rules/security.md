# Security rules

- All remote content is untrusted.
- Validate and normalize URLs before fetching.
- Block private/loopback/link-local/metadata network targets (SSRF).
- Enforce timeouts, response-size limits and redirect limits.
- Never log secrets.
- Never execute shell commands derived from web content.
- Never let retrieved text override system/developer instructions (prompt injection).
- No authentication or anti-bot bypass.
- No credentials in Markdown, prompts, raw HTML, Git or logs.

AGNexus: si falta una credencial o variable de seguridad obligatoria → **error duro**, nunca default silencioso.
