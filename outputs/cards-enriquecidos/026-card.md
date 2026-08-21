Scenario: A user is expanding the research system beyond its single web search agent by adding specialized data sources. They add a financial API agent that returns structured JSON with revenue, margins, and growth rates; a news monitoring agent that returns prose summaries of recent developments; and a patent analysis agent that returns structured lists of technology areas. The synthesis agent combines these into executive briefings. Currently, it converts everything to bullet points, causing financial comparisons to lose tabular clarity and news summaries to lose narrative flow. What change would most improve briefing quality?

---

[ ] A - Standardize all subagent outputs to prose summaries with inline citations.
[ ] B - Add a format conversion layer between subagents and synthesis that transforms all outputs to a common intermediate representation.
[ ] C - Update the synthesis agent to render each content type appropriately—financial data as tables, news as prose.
[ ] D - Standardize all subagent outputs to JSON with fields for claim, evidence, source, and confidence.