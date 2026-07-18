Scenario: Multi-Agent Research System You are building a multi-agent research system using the Claude Agent SDK. A coordinator agent delegates to specialized subagents: one searches the web, one analyzes documents, one synthesizes findings, and one generates reports. The system researches topics and produces comprehensive, cited reports. During testing, the document analysis subagent receives coordinator-selected PDFs and reports from an approved catalog, but it has a generic URL retrieval tool. It sometimes follows links inside documents to blogs, login pages, or duplicate HTML summaries, then cites those pages instead of the approved sources. You need to reduce these citation and scope errors while preserving access to approved source material. What change best addresses this?

---

[ ] A - Allow fetch_url for any link, then have synthesis discard citations whose domains are not in the approved catalog.
[ ] B - Replace fetch_url with a load_document tool that accepts catalog document IDs or approved URLs and validates before fetching.
[ ] C - Keep fetch_url available, but add prompt instructions warning the subagent never to open links found inside documents.
[ ] D - Give the document analysis subagent web search tools too, so it can independently confirm whether linked pages are relevant.