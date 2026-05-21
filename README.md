# Anthropic & Claude Code Courses


## Course Overview

- **Claude 101**  
  [https://anthropic.skilljar.com/claude-101](https://anthropic.skilljar.com/claude-101)  
  Learn how to use Claude for everyday work tasks, understand core features, and explore resources for more advanced learning on other topics.
- **Claude Code 101**  
  [https://anthropic.skilljar.com/claude-code-101](https://anthropic.skilljar.com/claude-code-101)  
  Learn how to use Claude Code effectively in your daily development workflow.
- **Introduction to Claude Cowork**  
  [https://anthropic.skilljar.com/introduction-to-claude-cowork](https://anthropic.skilljar.com/introduction-to-claude-cowork)  
  Learn to work alongside Claude on your real files and projects. This hands-on course covers the Cowork task loop, plugins and skills, file and research workflows, and how to steer multi-step work responsibly — so you're productive in your first week.
- **Claude Code in Action**  
  [https://anthropic.skilljar.com/claude-code-in-action](https://anthropic.skilljar.com/claude-code-in-action)  
  Integrate Claude Code into your development workflow
- **AI Fluency: Framework & Foundations**  
  [https://anthropic.skilljar.com/ai-fluency-framework-foundations](https://anthropic.skilljar.com/ai-fluency-framework-foundations)  
  Learn to collaborate with AI systems effectively, efficiently, ethically, and safely
- **Building with the Claude API**  
  [https://anthropic.skilljar.com/claude-with-the-anthropic-api](https://anthropic.skilljar.com/claude-with-the-anthropic-api)  
  This comprehensive course covers the full spectrum of working with Anthropic models using the Claude API
- **Introduction to Model Context Protocol**  
  [https://anthropic.skilljar.com/introduction-to-model-context-protocol](https://anthropic.skilljar.com/introduction-to-model-context-protocol)  
  Learn how to build Model Context Protocol servers and clients from scratch using Python. Master MCP's three core primitives—tools, resources, and prompts—to connect Claude with external services
- **AI Fluency for educators**  
  [https://anthropic.skilljar.com/ai-fluency-for-educators](https://anthropic.skilljar.com/ai-fluency-for-educators)  
  This course empowers faculty, instructional designers, and educational leaders to apply AI Fluency into their own teaching practice and institutional strategy.
- **AI Fluency for students**  
  [https://anthropic.skilljar.com/ai-fluency-for-students](https://anthropic.skilljar.com/ai-fluency-for-students)  
  This course empowers students to develop AI Fluency skills that enhance learning, career planning, and academic success through responsible AI collaboration.
- **Model Context Protocol: Advanced Topics**  
  [https://anthropic.skilljar.com/model-context-protocol-advanced-topics](https://anthropic.skilljar.com/model-context-protocol-advanced-topics)  
  Discover advanced Model Context Protocol implementation patterns including sampling, notifications, file system access, and transport mechanisms for production MCP server development.
- **Claude with Amazon Bedrock**  
  [https://anthropic.skilljar.com/claude-in-amazon-bedrock](https://anthropic.skilljar.com/claude-in-amazon-bedrock)  
  As part of an accreditation program created for AWS, Anthropic launched a first-of-its-kind training for AWS employees. Here's the full course so you can follow along.
- **Claude with Google Cloud's Vertex AI**  
  [https://anthropic.skilljar.com/claude-with-google-vertex](https://anthropic.skilljar.com/claude-with-google-vertex)  
  This comprehensive course covers the full spectrum of working with Anthropic models through Google Cloud's Vertex AI.
- **Teaching AI Fluency**  
  [https://anthropic.skilljar.com/teaching-ai-fluency](https://anthropic.skilljar.com/teaching-ai-fluency)  
  This course empowers academic faculty, instructional designers, and others to teach and assess AI Fluency in instructor-led settings.
- **AI Fluency for nonprofits**  
  [https://anthropic.skilljar.com/ai-fluency-for-nonprofits](https://anthropic.skilljar.com/ai-fluency-for-nonprofits)  
  This course empowers nonprofit professionals to develop AI fluency in order to increase organizational impact and efficiency while staying true to their mission and values.
- **Introduction to agent skills**  
  [https://anthropic.skilljar.com/introduction-to-agent-skills](https://anthropic.skilljar.com/introduction-to-agent-skills)  
  Learn how to build, configure, and share Skills in Claude Code — reusable markdown instructions that Claude automatically applies to the right tasks at   the right time. This course takes you from creating your first Skill to distributing them across teams and troubleshooting common issues.
- **Introduction to subagents**  
  [https://anthropic.skilljar.com/introduction-to-subagents](https://anthropic.skilljar.com/introduction-to-subagents)  
  Learn how to use and create sub-agents in Claude Code to manage context, delegate tasks, and build specialized   workflows that keep your main conversation clean and focused.
- **AI Capabilities and Limitations**  
  [https://anthropic.skilljar.com/ai-capabilities-and-limitations](https://anthropic.skilljar.com/ai-capabilities-and-limitations)  
  An introductory course about how AI works
- **AI Fluency for Small Businesses**  
  [https://anthropic.skilljar.com/ai-fluency-for-small-businesses](https://anthropic.skilljar.com/ai-fluency-for-small-businesses)  
  This course empowers small businesses to develop AI fluency in order to increase organizational impact and efficiency while staying true to their mission and values.


## Learning Resources

- **Anthropic Courses**  
  [https://anthropic.skilljar.com](https://anthropic.skilljar.com)
- **Anthropic Academy**  
  [https://www.anthropic.com/learn](https://www.anthropic.com/learn)
- **Anthropic on YouTube**  
  [https://www.youtube.com/@anthropic-ai/playlists](https://www.youtube.com/@anthropic-ai/playlists)
- **Claude on YouTube**  
  [https://www.youtube.com/@claude/playlists](https://www.youtube.com/@claude/playlists)


## What I did in this repository (Changelog)

- My **objective** was to have a nice **overview of Anthropic learning resources** containing videos. It's helpful to have experts explaining basic concepts and give some insights. The focus was originally on Claude Code (not just Claude or other LLMs or integrations).
- That time (2026-05-19), I discovered **18 (video) courses** listed at Anthropic Academy and inside **Skilljar**.
- I discovered some courses on **Skilljar** (mostly with XMLish overview, one time with Markdown and embedded HTML). Also, some courses are on **YouTube**, some on account anthropic-ai and some on account claude. Some categorized with a playlist, some with a course, some without any. The data is insinde directory [sources](sources).
- To get an **overview of courses**, I used **n8n** and a LLM to extract title, link and description of the individual courses. The n8n workflow is inside [n8n-workflows](n8n-workflows).
- After some days, I finally had time to **use Claude Code** itself.
    - To generate an overview, I started Claude on Linux terminal and prompted "I want to scrape https://anthropic.skilljar.com to have an overview of course contents. The later objective would be to generate learning paths based on the contens of course descriptions. There is already an overview in ./data/courseOverview.json."
    - First some chat ping-pong, because I used terminal environment variables to set endpoint, API key, ... and Claude Code could not access it. (Side quest: Let AI write a book Mythos 42, where it states to have no access. More than beginner psychology level, the magic mirror controls the panopticon pushing interesting emotions.)
    - Strange: When installing python packages, it seems like it used the default environment instead of creating a new one. Not checked yet.
    - Cool, it created:
        - .env
        - .env.example
        - data/courseDetails.json — 18 courses, each with:                                                                                                                                                                 
            - stats (lecture count, video hours, quiz count)                                                                                                                                                                 
            - en — title, subtitle, sections with titles/descriptions/lesson counts                                                                                                                                          
            - de — same structure, fully translated   
        - scripts/
        - Claude Code: "3 courses (claude-101, introduction-to-agent-skills, introduction-to-subagents) had no embedded section data on Skilljar so they got title/description only. The new ai-fluency-for-pk12-educators course that   
  exists on Skilljar but wasn't in your overview is also not included — worth adding to courseOverview.json if you want it."
        - Interesting: No CLAUDE.md, skills etc., state may be all in ~/.claude

## Contact

adrian (at) [agnion.ai](https://www.agnion.ai)