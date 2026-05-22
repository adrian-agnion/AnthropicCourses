---
path_ids: api-developer-aws, api-developer-gcp
title: Claude on Cloud Platforms — Amazon Bedrock & Google Cloud Vertex AI
level: intermediate
audience: AWS developers, GCP developers, cloud engineers, ML engineers, solutions architects
core_concepts: same full curriculum as direct API path (auth, prompting, tool use, RAG, MCP, agents) via Bedrock or Vertex AI SDKs and consoles; 85 lectures / 8h each
---

## Image Generation Prompt

A split-panel cloud architecture illustration showing Claude running on two major cloud platforms. Bold, clean, and technically precise. Background: deep space blue #0B1120.

**Left Panel — Amazon Bedrock (AWS orange #FF9900 accent):**
An AWS cloud infrastructure diagram with AWS logo badge and *"Amazon Bedrock"* label at top.
- Bedrock console interface thumbnail: dark sidebar, model selector showing "Claude" highlighted
- Floating terminal with SDK code snippet: `bedrock_runtime.invoke_model(modelId="claude...", body=...)`
- Data flow arrows: developer code → Bedrock API endpoint → Claude model → response object
- Floating AWS service icons: IAM lock, S3 bucket, Lambda symbol, CloudWatch eye
- Bottom badge: *"85 lectures · 8h · AWS accreditation-level content"*

**Right Panel — Google Cloud Vertex AI (GCP blue #4285F4 accent):**
A GCP cloud infrastructure diagram with Google Cloud logo badge and *"Vertex AI"* label at top.
- Vertex AI console thumbnail: Google Material Design, Model Garden view with Claude card
- Floating terminal with SDK code: `aiplatform.init(project=...) · model.predict(instances=[...])`
- Data flow arrows: developer code → Vertex AI API endpoint → Claude model → response object
- Floating GCP service icons: BigQuery BQ logo, Cloud Storage bucket, Cloud Run gear, Cloud Logging scroll
- Bottom badge: *"85 lectures · 8h · Google Cloud curriculum"*

**Center Column — Shared Foundation:**
A vertical divider strip between the two panels shows what is platform-agnostic:
- Claude shell-wave logo mark centered
- *"Same Curriculum"* badge with a checkmark
- Bullet list: *Prompting · Tool Use · RAG · MCP · Agent Architectures · Computer Use*
- MCP plug icon with label: *"Platform-agnostic MCP integration"*

**Bottom strip — Path continuation:**
Both panels converge at the bottom: an arrow from each panel points to a shared MCP server node below, labeled *"Extend with MCP (recommended next step)."*

**Style:** Clean cloud architecture illustration. Bold platform brand colors. Symmetric two-column layout with a shared center column. Flat icons with subtle depth. Technical but accessible.

**Palette:** Space blue #0B1120 · AWS orange #FF9900 · GCP blue #4285F4 · Shared teal #00BCD4 · Claude violet #7B2FBE · White #F1F5F9

**Format:** 16:9 landscape. Split-screen comparison banner.

**Mood:** Professional, scalable, enterprise-ready. Claude meets you on the cloud platform you already use.
