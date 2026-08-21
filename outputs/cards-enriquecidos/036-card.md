Scenario: After deployment, you find that 12% of extractions contain semantic errors that pass JSON schema validation (e.g., a duration like "30 minutes" incorrectly placed in an ingredient quantity field). Human reviewers have capacity to check only 20% of extractions. Which approach most effectively allocates reviewer attention?

---

[ ] A - Have the model output field-level confidence scores, then calibrate review thresholds using a labeled validation set.
[ ] B - Randomly sample 20% of extractions for review, using corrections to track accuracy and identify error patterns.
[ ] C - Prioritize review of all extractions where required fields are empty or explicitly marked as not found.
[ ] D - Review all extractions from documents with formatting anomalies such as unusual layouts or mixed content types.