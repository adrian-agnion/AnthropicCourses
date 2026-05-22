---
path_id: mcp-developer
title: Building MCP Servers & Clients
level: intermediate
audience: backend developers, platform engineers, integration engineers, API developers, tooling engineers
core_concepts: MCP architecture, Python SDK, server + client implementation, tools/resources/prompts primitives, sampling, progress notifications, file roots, STDIO vs StreamableHTTP
---

## Image Generation Prompt

Please create a 3D Minion. Color of all Minions is lavender (#b985e2), and its overalls are eastern blue (#35a1bd). This Minion is a master plumber-engineer building an MCP server from scratch. It is wearing a hard hat over its goggles and a tool belt loaded with colorful cables and wrenches over its overalls. Background: deep dark purple #170538 with faint technical-blueprint lines.

**The Workshop:**
A cozy engineering workshop — workbench covered in tools, components, and one half-eaten banana. The MCP server-in-progress sits at the center of the workbench like an open machine: a box with visible internals, three color-coded module shelves, and colorful pipes running between them. The Minion has its hands inside the machine with the focused expression of someone who absolutely knows what they are doing (mostly).

**The Three Primitive Module Shelves inside the server:**

**Top shelf — Tools Module (green #22C55E):**
A row of callable function cards hanging like tools on a pegboard. Each has a schema label: `search(query: str)`, `execute_code(lang, code)`, `query_db(sql)`. A small placard: *"Claude can call dese."* One tool card has fallen off its hook and the Minion has not noticed.

**Middle shelf — Resources Module (amber #F59E0B):**
Readable data source cards stacked neatly: a file card, a database row card, an API endpoint card. Organized with sticky-note labels. A placard: *"Claude can read dese."* Everything here is suspiciously tidy compared to the rest of the workshop.

**Bottom shelf — Prompts Module (blue #3B82F6):**
Template cards with yellow sticky-note variable placeholders: `{user_query}`, `{context}`, `{format}`. A placard: *"Claude can compose wit dese."* The Minion has accidentally stuck one sticky note to its own hand and has not noticed.

**Left side of workbench — Development tools:**
- A Python package box labeled `pip install mcp` with a green installed checkmark.
- The MCP Inspector tool depicted as an actual magnifying glass the Minion has propped up to peer into the server's internals. A JSON output paper trail rolls out from underneath it.
- A terminal on a small screen: `mcp run server.py` → *"Server running. Tools: 3. Resources: 2. Prompts: 1."*

**Right side of workbench — Production features:**
- A sampling meter (gauge dial) labeled "AI Cost Management" pointing to "EFFICIENT." The Minion has taped a star next to this.
- A progress notification bar with event icons streaming — a small bell rings every few seconds.
- A file roots tree behind a tiny locked gate labeled "Secure Boundaries."
- A transport toggle switch: STDIO ←→ StreamableHTTP. Currently set to STDIO. A note reads: *"Change when going to production (ask someone)."*

**On the floor near the Minion's feet:**
A Claude Code terminal icon and an API client icon connected to the server via color-coded cables. The cables are slightly tangled but connected correctly. A tag on the cable bundle reads: *"MCP Clients that eat from your server."*

**Style:** High-quality 3D Minion in the Illumination Studios style. Workshop atmosphere — warm tool-light overhead. Lavender skin, eastern blue overalls, hard hat, tool belt. The server machine has a warm glow coming from inside. 3D Cartoon physics — cables slightly alive, tools slightly oversized. Dark purple #170538 background.

**Text overlay:** Two lines of bold clean sans-serif text centered at the bottom over a dark semi-transparent band:
- Line 1 (small, wide letter-spacing): LEARNING PATH
- Line 2 (large, prominent): Building MCP Servers & Clients
Both lines in white (#F0F4F8) with a subtle violet drop-shadow.

**Palette:** #170538 background · Lavender #b985e2 · Eastern blue #35a1bd · Green #22C55E · Amber #F59E0B · Blue #3B82F6 · Teal #2DD4BF · Orange #EA580C · Banana yellow #FFD166

**Format:** 1:1 square. Course tile / social media card.

**Mood:** Crafty, expert, deeply satisfied. The Minion is building the connective tissue of the AI world. One pipe at a time.
