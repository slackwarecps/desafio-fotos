Scenario: Your agent needs to insert a new helper function into the middle of a 150-line utility module, between two existing functions. The Edit tool fails because its `old_string` parameter cannot find unique text to match — the file has repetitive docstrings, variable names, and structural patterns. What's the most reliable way to complete this insertion?

---

[ ] A - Use Edit with an extremely long `old_string` capturing 30+ lines of context to guarantee uniqueness
[ ] B - Use Edit's `replace_all` parameter to target a common pattern and embed the new function in the replacement text
[ ] C - Use Bash to append the function definition to the end of the file using heredoc syntax
[ ] D - Use Read to load the file, add the function at the appropriate location, then Write the updated file
