Scenario: The agent verifies customer identity through a multi-step process before resetting passwords. During testing, you notice that after the customer answers the third verification question, the agent asks them to provide their name again, as if the earlier exchange never happened. What's the most likely cause of this behavior?

---

[ ] A - The verification tool is clearing the agent's internal state after each successful validation step.
[ ] B - The prompt lacks instructions telling Claude to remember information across multiple exchanges.
[ ] C - The conversation history isn't being passed in subsequent API requests.
[ ] D - Claude's memory retention is limited to two conversational turns by default, requiring explicit configuration to extend it.