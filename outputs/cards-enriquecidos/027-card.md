Scenario: A contract is too long to fit in one context window, and you need fields from across the whole document. The dependable approach is to:

---

[ ] A - Truncate the document to what fits and extract from the first part.
[ ] B - Chunk the document with slight overlap, extract per chunk, then merge and reconcile the fields.
[ ] C - Summarize the document first, then extract from the summary.
[ ] D - Raise the temperature so the model fills in the missing parts.