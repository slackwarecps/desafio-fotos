Scenario: An engineer who just joined the team asks the agent to help them understand the authentication and authorization architecture before making security improvements. The codebase has 800+ files across multiple services. What exploration strategy will most effectively build understanding, given Claude built-in tools and context limits?

---

[ ] A - Read any CLAUDE.md and README files first, then ask the engineer to specify which 10-15 files are most important for understanding the auth system.
[ ] B - Launch parallel subagents to explore different services simultaneously, then synthesize their findings into an architectural overview.
[ ] C - Use Grep to find authentication entry points, read those files, then follow imports and function calls to map the auth flow incrementally.
[ ] D - Read all files containing "auth", "login", "permission", or "token" in their content or filename.