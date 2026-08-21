Scenario: The synthesis agent receives summarized findings from the web search and document analysis agents, then passes a consolidated summary to the report generator. During testing, you discover the generated reports make factual claims without proper citations—the report generator cannot attribute statements to their original sources because that metadata was lost during the summarization steps. What's the most effective approach to ensure proper source attribution in the final reports?

---

[ ] A - Have each agent output structured data separating content summaries from source metadata (URLs, document names, page numbers).
[ ] B - Have the report generator query the web search agent to re-locate sources for claims in the final report.
[ ] C - Instruct the synthesis agent to embed source references inline within its summary text using a consistent citation format.
[ ] D - Skip summarization and pass full raw outputs from web search and document analysis directly to the report generator.