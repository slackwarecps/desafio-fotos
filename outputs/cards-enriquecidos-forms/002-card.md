Scenario: After your daily batch of 10,000 documents completes, 300 documents (3%) failed with "`context_length_exceeded`" errors. The results file identifies each failure by `custom_id`. What's the most cost-effective approach to process these failures?

---

[ ] A - Reprocess the entire batch with prompt caching enabled to reduce the cost of retrying requests with identical system prompts
[ ] B - Resubmit only the 300 failed documents after chunking them into smaller pieces, then combine the partial extractions
[ ] C - Resubmit the entire 10,000 document batch using a model tier with a larger context window
[ ] D - Increase the `max_tokens` parameter for the 300 failed documents and resubmit them in a new batch
