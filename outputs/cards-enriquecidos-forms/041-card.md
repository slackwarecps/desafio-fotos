Scenario: When implementing your `lookup_order` MCP tool, the backend sometimes returns errors (e.g., "Order not found" or temporary database failures). What is the correct pattern for communicating these errors back to the agent?

---

[ ] A - Log the error server-side and return an empty result to avoid confusing the modelB.Return the error message in the tool result content with the isError flag set to trueC.Throw an exception from the tool handler so the agent framework can catch and log itD.Return a success response with a "status" field indicating the error type
[ ] B - Return the error message in the tool result content with the isError flag set to trueC.Throw an exception from the tool handler so the agent framework can catch and log itD.Return a success response with a "status" field indicating the error type
[ ] C - Throw an exception from the tool handler so the agent framework can catch and log itD.Return a success response with a "status" field indicating the error type
[ ] D - Return a success response with a "status" field indicating the error type
