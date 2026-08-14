Scenario: Your agent is handling a billing dispute. After calling `get_customer` and `lookup_order`, it identifies that the dispute involves a promotional pricing error requiring manager approval—beyond the agent's authorization level. How should the workflow handle this mid-process escalation?

---

[ ] A - Call `escalate_to_human` passing only the customer's original message.B.Compile a structured handoff with customer details, order info, and the identified issue before calling `escalate_to_human`.C.Attempt the refund with `process_refund` anyway, escalating only if the system rejects the transaction.D.Persist the complete conversation and tool response history to a database, then call `escalate_to_human` with a reference ID.
[ ] B - Compile a structured handoff with customer details, order info, and the identified issue before calling `escalate_to_human`.C.Attempt the refund with `process_refund` anyway, escalating only if the system rejects the transaction.D.Persist the complete conversation and tool response history to a database, then call `escalate_to_human` with a reference ID.
[ ] C - Attempt the refund with `process_refund` anyway, escalating only if the system rejects the transaction.D.Persist the complete conversation and tool response history to a database, then call `escalate_to_human` with a reference ID.
[ ] D - Persist the complete conversation and tool response history to a database, then call `escalate_to_human` with a reference ID.
