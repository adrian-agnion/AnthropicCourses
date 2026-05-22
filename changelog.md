# Anthropic & Claude Code Courses

To pick your best-fit learning path, check the site 🧠⚡ **[Anthropic Course Learning Paths](data/learningPaths.md)** ⚡🧠.


## What I did in this repository (Changelog)

- This is my second try with **Claude Code**, first try was a success — generating an **OpenAPI** file for an **n8n backend** I know inside out.
- My **objective** was to have a nice **overview of Anthropic learning resources** (<https://www.anthropic.com/learn>) containing videos. It's helpful to have experts explaining basic concepts and give some insights. The focus was originally on Claude Code (not just Claude or other LLMs or integrations).
- That time (2026-05-19), I discovered **18 (video) courses** listed at Anthropic Academy and inside **Skilljar**.
- I discovered some courses on **Skilljar** (mostly with XMLish overview, one time with Markdown and embedded HTML). Also, some courses are on **YouTube**, some on account anthropic-ai and some on account claude. Some categorized with a playlist, some with a course, some without any. The data is insinde directory [sources](sources).
- To get an **overview of courses**, I used **n8n** and a LLM to extract title, link and description of the individual courses. The n8n workflow is inside [n8n-workflows](n8n-workflows).
- After some days, I finally had time to **use Claude Code** itself.
    - To generate an overview, I started Claude on Linux terminal and prompted "I want to **scrape** https://anthropic.skilljar.com to have an overview of course contents. The later objective would be to generate learning paths based on the contens of course descriptions. There is already an overview in ./data/courseOverview.json."
    - **First some chat ping-pong**, because I used terminal **environment variables to set endpoint**, API key, ... and Claude Code could not access it. (Side quest: Let AI write a book Mythos 42, where it states to have no access. More than beginner psychology level, the magic mirror controls the panopticon pushing interesting emotions.)
    - Strange: When **installing python packages**, it seems like it used the default environment instead of creating a new one. Not checked yet.
    - Cool, **it created**:
        - .env
        - .env.example
        - **data/courseDetails.json** — 18 courses, each with:                                                                                                                                                                 
            - stats (lecture count, video hours, quiz count)                                                                                                                                                                 
            - en — title, subtitle, sections with titles/descriptions/lesson counts                                                                                                                                          
            - de — same structure, fully translated <- Could also be done afterwards ...
        - scripts/
        - Claude Code: "**3 courses** (claude-101, introduction-to-agent-skills, introduction-to-subagents) had **no embedded section data** on Skilljar so they got title/description only. The new ai-fluency-for-pk12-educators course that
  exists on Skilljar but wasn't in your overview is also not included — worth adding to courseOverview.json if you want it."
        - Interesting: No CLAUDE.md, skills etc., state may be all in ~/.claude
- Claude Code prompt: "**Add** [to] ai-fluency-for-educators to courseOverview.json"
- Claude Code prompt: "Could you **check** <https://anthropic.skilljar.com/ai-fluency-for-pk12-educators> and <https://anthropic.skilljar.com/ai-fluency-for-educators>? My browser shows me only the second one."
    - "courseOverview.json is back to 18 courses — all publicly listed ones. The pk12 course **exists behind a login wall** so it was a false positive from the embedded JS bundle."
- I: "could you **make a note** somewhere in the repository about those 2 overlapping courses and data sources? and also update the 2 files in data directory.
"
- I: **do not touch** the README.md and other files you did not create.
    - CC: Good — the README.md is already clean (the user reverted my addition). The _notes are in both data files already.
    - CC: Both data files have their _notes. The README.md is untouched. Done.
- I: which courses do have **missing data?**
    - CC: [...] claude-101, introduction-to-agent-skills, introduction-to-subagents
- I: All 3 courses are **available on YouTube**. Try to **get the course overview** there.
    - CC: **Lots** of playlist and YouTube **scraping** commands/executions
    - Note: Lots of unneccessary requests. Why did it not directly check the YouTube URLs on anthropic?
    - I, controlling: "Yes, **try to use less requests**. **there are** 3 videos already listed on the course overview. use that as a base and just get the basic data."
- I (new claude session): Check the data in directory ./data. **I want learning paths** for different learing stages and roles. Highest priority: Someone wnats to learn and use Claude Code. Create learning paths on which courses to take   
  to get familar with Claude Code and also other paths, e.g. handling Claude itself or using it as an educator. Create a new md file or json file or something better (maybe both?)  with data about how to start
  at a learning level and go through different courses to get the required knowledge to reach a state to be able to use the Claude variants.
    - CC: data/learningPaths.json and data/learningPaths.md [...]
- I: could you **sub-divide** the section "Course Overview" in the **README.md** into "Claude Code" and other sub-sections?
- I: have you **included the contets in ./sources?** If not, do so for your own generated or extended md files.
    - I: revert the changes in sources/learningPaths.notes.md.txt. If you decide to, include the contents there into your own created md files or modified ones
    - CC: Done. The file is removed and nothing needed to be merged since it was an exact duplicate of data/learningPaths.md.
- I: (at <https://gemini.google.com/>): what is the max promt length for nano banana?
    - G: For the Nano Banana image generation tool, the prompt character limit is 10,000 characters.
- I: (to myself): Planning to generate a nice ovwrview image
- I: I read the character limit for creating an image is around 10,000 characters. To have some variants for me, let's say it is around 8,000 characters. So let's create a directory "./images". I need some image   
  prompt templates to focus on Clause Code, secondary to explain different (other) learning paths for Claude in general. Focus on the data inside data/learningPaths.json and use the main learning ideas to       
  creete textural data best to be used to create images afterwards, focusing on the Claude Code learning paths.
    - CC started to create 10 prompt files in parallel. That was not expected, I assumed maybe 3 files. Let's check.


## Contact

Adrian Wilke - adrian (at) [agnion.ai](https://www.agnion.ai)