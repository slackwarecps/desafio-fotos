Scenario: Context Window Trade-offs Your team is building a document search system where users can ask questions about large documents. You can use a context window that supports 100K tokens (Claude 3.5 Sonnet) or a smaller window (32K tokens, Claude 3.5 Haiku) which is 5x cheaper. Initial testing shows that 80% of documents fit within 32K tokens, but the remaining 20% need truncation. What approach makes sense?

---

[ ] A - Use Haiku exclusively; save the money and accept truncation as a trade-off for all cases.
[ ] B - Use Sonnet exclusively; the larger window provides consistent results and the cost is acceptable for production.
[ ] C - Route small documents to Haiku, large documents to Sonnet, managing differences in models' reasoning.
[ ] D - Use Haiku by default, and programmatically chunk large documents so they always fit the smaller window.
