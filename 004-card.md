Scenario: Multi-Model Orchestration Strategy You are architecting a system that needs to handle both high-latency, highly-accurate tasks (research synthesis) and low-latency, cost-sensitive tasks (content moderation). A single unified model can handle both but costs 3x more than using two specialized models. The research team strongly prefers unified experiences, but operations is concerned about budget impact. What should you recommend?

---

[ ] A - Use the unified model for both workloads; the better accuracy for moderation justifies the cost.
[ ] B - Split into two models, use the expensive one only for research, route moderation to a cheaper alternative.
[ ] C - Use the unified model but add a caching layer to reduce duplicate queries across workloads.
[ ] D - Implement a cost-aware router: direct to unified model when latency permits, fall back to cheaper model under load.
