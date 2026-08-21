Scenario: Your extraction pipeline processes contracts that frequently include amendments. When a contract contains both original terms and later amendments (e.g., original clause specifies "30-day payment terms" while Amendment 1 changes this to "45 days"), the model inconsistently extracts one value or the other with no indication of which applies. What's the most effective approach to improve extraction accuracy for documents with amendments?

---

[ ] A - Redesign the schema so amended fields capture multiple values, each with source location and effective date.
[ ] B - Add prompt instructions to always extract the most recent amendment value and ignore superseded original terms.
[ ] C - Preprocess documents with a classifier that identifies and removes superseded sections before the main extraction step.
[ ] D - Implement post-extraction validation using pattern matching to detect amendments and flag those extractions for manual review.