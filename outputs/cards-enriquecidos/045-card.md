Scenario: After investigating a billing dispute over 25+ turns, you've identified that duplicate charges occurred due to a payment gateway timeout triggering retry logic. The required refund ($847) exceeds your $500 authorization limit. You need to call `escalate_to_human`, and the human agent won't have access to your conversation transcript. What context should you pass to enable effective resolution?

---

[ ] A - The customer's original complaint verbatim plus the tool result excerpts showing duplicate transactions.
[ ] B - A structured summary: customer ID, root cause, refund amount, and recommended action.
[ ] C - The complete conversation transcript with all tool results.
[ ] D - Your diagnosis and the refund amount only.