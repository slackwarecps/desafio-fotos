Scenario: Your extraction pipeline processes restaurant menus and must output structured JSON with fields for item names, descriptions, prices, and dietary tags. Some menus use inconsistent formatting—prices as "$12" vs "12.00", dietary info as icons vs text. What's the most reliable approach?

---

[ ] A - Use separate extraction calls for each field to ensure consistent handling of each type.
[ ] B - Extract data as-is and normalize formats in post-processing code after Claude returns.
[ ] C - Request multiple extraction attempts per document and select the most common format.
[ ] D - Define a strict output schema and include format normalization rules in your prompt.