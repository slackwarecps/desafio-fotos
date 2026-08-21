Scenario: Your pipeline uses a tool called `extract_metadata` with a JSON schema for paper details. You've also defined `lookup_citations` and `verify_doi` tools for enrichment. During testing, you notice that when users include requests like "extract the metadata and tell me how cited it is," Claude sometimes calls `lookup_citations` first, which fails because it needs the DOI that `extract_metadata` would provide. What's the most effective way to ensure structured metadata extraction happens first?

---

[ ] A - Set `tool_choice` to "any" so Claude must use a tool, combined with system prompt instructions prioritizing `extract_metadata`.
[ ] B - Set `tool_choice` to "auto" and reorder the tool definitions so `extract_metadata` appears first in the tools array, since Claude prioritizes earlier-listed tools.
[ ] C - Set `tool_choice` to {"type": "tool", "name": "`extract_metadata`"} and process the enrichment requests in subsequent turns after receiving the extracted metadata.
[ ] D - Set `tool_choice` to {"type": "tool", "name": "`extract_metadata`"} for every API call in the pipeline, ensuring Claude always extracts metadata before any enrichment can occur.