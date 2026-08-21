Scenario: During a billing dispute resolution, your agent successfully retrieves customer info via `get_customer` and order details via `lookup_order`, but when attempting to call `process_refund`, the tool returns a timeout error. The agent has enough information to explain the charges and verify refund eligibility, but cannot actually process the refund due to the backend failure. What approach best balances first-contact resolution with appropriate error handling?

---

[ ] A - Escalate immediately to a human agent since the refund action cannot be completed
[ ] B - Implement automatic retries with exponential backoff for `process_refund`, keeping the conversation open until the refund is successfully processed
[ ] C - Explain the billing, confirm refund eligibility, acknowledge the system issue preventing immediate processing, and offer escalation or retry later
[ ] D - Confirm the refund will be processed and close the conversation, since the system has all necessary information to complete it automatically