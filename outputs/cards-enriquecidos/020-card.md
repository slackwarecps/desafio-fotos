Scenario: Production logs reveal inconsistent error handling: when `lookup_order` fails, the agent sometimes retries 5+ times (wasteful when the order ID doesn't exist), sometimes escalates immediately (premature for temporary network issues), and sometimes asks users for clarification (inappropriate when the issue is a backend permission error). Investigation shows your MCP tool returns uniform error responses: {"isError": true, "content": [{"type": "text", "text": "Operation failed"}]}. The agent cannot distinguish between error types. What's the most effective improvement?

---

[ ] A - Enhance error responses with structured metadata: include errorCategory (transient/validation/permission), isRetryable boolean, and a description of what caused the failure.
[ ] B - Create an `analyze_error` MCP tool the agent calls after any failure to determine the error category and recommended action.
[ ] C - Implement retry logic with exponential backoff in your MCP server for all errors, returning to the agent only after retries are exhausted.
[ ] D - Add few-shot examples to the system prompt demonstrating how to interpret error message patterns and select appropriate responses for each.