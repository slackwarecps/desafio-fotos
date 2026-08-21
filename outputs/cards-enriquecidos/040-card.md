Scenario: After the web search agent finds 25 sources (120K tokens of raw content), the document analysis agent extracts key insights (15K tokens), and the synthesis agent produces a coherent narrative draft (3K tokens), the coordinator must pass context to the report generation agent for the final output with proper source citations. What context-passing strategy provides the best balance of completeness and efficiency?

---

[ ] A - Pass only the synthesis draft and have a separate post-processing pipeline match claims to sources and insert citations after the report is generated.
[ ] B - Pass the synthesis draft along with a structured source index that maps key claims to their source URLs and relevant excerpts.
[ ] C - Pass a condensed summary of all prior stages that preserves the main findings and attributes them to sources by name only.
[ ] D - Pass the full accumulated context from all prior agents.