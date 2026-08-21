Scenario: When analyzing complex legal cases that cite multiple precedents, the document analysis subagent processes each sequentially. A landmark case citing 12 precedents takes over 3 minutes to analyze completely. What's the most effective way to reduce this latency while preserving the coordinator's ability to monitor and debug the system?

---

[ ] A - Implement a message queue where precedent analysis tasks are processed asynchronously by a pool of worker agents.
[ ] B - Create a recursive agent hierarchy where analysis agents subdivide work among child agents until reaching single-precedent granularity.
[ ] C - Have the coordinator spawn parallel document analysis subagents, each handling a subset of precedents, then aggregate results before synthesis.
[ ] D - Enable the document analysis subagent to spawn its own specialized subagents dynamically when it encounters cases with many citations.