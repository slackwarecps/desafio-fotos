Scenario: A field the schema expects is simply not present in the source document. The extractor should:

---

[ ] A - Fill the field with a plausible value inferred from the rest of the document.
[ ] B - Return null for that field and mark it as not found, leaving the rest of the extraction intact.
[ ] C - Fail the entire extraction because one field is missing.
[ ] D - Repeat the previous record value for that field.