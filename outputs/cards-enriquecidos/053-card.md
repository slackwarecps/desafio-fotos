Scenario: The web search agent has gathered several relevant sources for a research topic. The document analysis agent now needs to examine these sources. How does information typically flow between these two specialized subagents?

---

[ ] A - The agents communicate through an event-driven message queue, with the document analysis agent subscribing to web search completion events.
[ ] B - The web search agent directly invokes the document analysis agent, passing the discovered sources as parameters.
[ ] C - The coordinator agent receives the web search agent's output and includes relevant findings in the prompt when invoking the document analysis agent.
[ ] D - Both agents access a shared memory store where the web search agent writes findings and the document analysis agent reads them.