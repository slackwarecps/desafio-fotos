Scenario: A single source file is thousands of lines long and the agent needs one function from it. The agent should:

---

[ ] A - Read the entire file into context to be thorough.
[ ] B - Search within the file for the function and read only that region and its immediate dependencies.
[ ] C - Read the first few hundred lines and stop.
[ ] D - Reformat the file so it is easier to scan.