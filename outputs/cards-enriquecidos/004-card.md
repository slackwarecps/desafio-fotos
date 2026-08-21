Scenario: An engineer asks the agent to find all callers of a function before removing it. The function is defined in a core library but is also exposed through wrapper modules that rename the function for domain-specific use (e.g., calculateTax in the library becomes computeOrderTax in the orders module). What exploration strategy will most reliably identify all callers?

---

[ ] A - Read the library and wrapper modules to identify all exposed names for the function, then Grep for each name across the codebase.
[ ] B - Use Grep to find all files that import from the library or wrapper modules, then read each file to check whether it uses the function.
[ ] C - Use Grep to search for the function's original name across the codebase.
[ ] D - Search for the function name in project documentation to understand intended usage patterns and navigate to documented integration points.