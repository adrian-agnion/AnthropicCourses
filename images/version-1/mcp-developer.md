---
path_id: mcp-developer
title: Building MCP Servers & Clients
level: intermediate
audience: backend developers, platform engineers, integration engineers, API developers, tooling engineers
core_concepts: MCP architecture, Python SDK, server + client implementation, tools/resources/prompts primitives, sampling, progress notifications, file roots, STDIO vs StreamableHTTP transport
total_hours_required: 2.1h
---

## Image Generation Prompt

A builder's workshop illustration showing an MCP server being constructed from its component parts. The aesthetic is engineering and craft — a cutaway diagram revealing the server's internal structure while a developer assembles it. Background: dark warm charcoal #16100A.

**Main workspace — The MCP Server Under Construction:**
A large central panel shows an MCP server as an open modular system — like a cutaway engineering diagram with visible internal shelves and modules.

**Three Core Primitive Modules (color-coded internal shelves):**

- 🔧 **Tools Module** (top shelf, green #22C55E): A row of callable function cards, each with a parameter schema label visible. Icons: wrench, gear, API connector. A small note: *"Claude can call these functions."*
- 📚 **Resources Module** (middle shelf, amber #F59E0B): Readable data sources displayed as cards — a file card, a database row card, an API endpoint card. Icons: scroll, folder, database. Note: *"Claude can read these."*
- 💬 **Prompts Module** (bottom shelf, blue #3B82F6): Reusable template cards with slot variables highlighted. Icons: speech bubble, template card with variable placeholders. Note: *"Claude can compose with these."*

**Left sidebar — Development & Testing:**
- Python logo with `pip install mcp` command
- MCP Inspector tool icon (magnifying glass + JSON output panel) — *"Built-in server testing"*
- Terminal showing: `mcp run server.py` — green "Server running on port 8080" response

**Right sidebar — Production Features:**
- Sampling diagram: bidirectional arrows between server and Claude with a cost-meter icon. Label: *AI cost management via sub-calls*
- Progress bar with streaming event icon. Label: *Real-time progress notifications for UX*
- File roots tree with a lock icon. Label: *Secure file access boundaries*
- Transport selector: "STDIO" ⟷ "StreamableHTTP" toggle with use-case annotations

**Top — Client Connection view:**
Two client icons at the top connect downward to the server via the MCP protocol line: a Claude Code terminal icon (left) and an API application icon (right). A dashed line with "MCP Protocol" label connects them to the server below.

**The Builder:**
A developer figure crouches at the base of the server structure, hands placing a new module card into an empty slot. Focused, competent expression. Small floating quality indicators: green checkmarks on completed modules, a passing test suite icon, an inspector handshake badge.

**Style:** Engineering workshop meets tech product illustration. Warm dark background contrasts with vivid module colors. Cutaway/exploded-view aesthetic for the server internals. Clean, precise, builder-focused. No photorealism.

**Palette:** Warm charcoal #16100A · Green #22C55E · Amber #F59E0B · Blue #3B82F6 · Teal #2DD4BF · Orange #EA580C · White #FFF7ED

**Format:** 16:9 landscape. Course hero banner.

**Mood:** Constructive, expert, satisfying. You're building the connective tissue that links AI to the real world.
