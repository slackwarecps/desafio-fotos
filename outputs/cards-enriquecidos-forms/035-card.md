Scenario: When the agent calls `lookup_order` and receives order details showing the item was purchased 45 days ago, how does the agentic loop determine whether to call `process_refund` or `escalate_to_human` next?

---

[ ] A - The orchestration layer automatically routes to the next tool based on the order's status field.B.The agent follows a pre-configured decision tree mapping order attributes to specific tool calls.C.The order details are added to the conversation and the model reasons about which action to take.D.The agent executes the remaining steps in a tool sequence planned at the start of the request.
[ ] B - The agent follows a pre-configured decision tree mapping order attributes to specific tool calls.C.The order details are added to the conversation and the model reasons about which action to take.D.The agent executes the remaining steps in a tool sequence planned at the start of the request.
[ ] C - The order details are added to the conversation and the model reasons about which action to take.D.The agent executes the remaining steps in a tool sequence planned at the start of the request.
[ ] D - The agent executes the remaining steps in a tool sequence planned at the start of the request.
