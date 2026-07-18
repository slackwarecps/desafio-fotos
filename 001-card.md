Scenario: Structured Data Extraction You are building a structured data extraction system using Claude. The system extracts information from unstructured documents, validates output using JSON schemas, and maintains high accuracy. It must handle edge cases gracefully and integrate with downstream systems. Your product has two document queues: customer onboarding forms that must populate an eligibility screen while an operations specialist is waiting, and 40,000 archived contracts used for a dashboard due next week. Finance asks whether the lower-cost processing path should replace the current real-time calls for both queues. What should you recommend?
---
[ ] A - Route onboarding forms to batches first, then fall back to synchronous calls whenever pending jobs exceed a threshold.
[ ] B - Move both queues to the Message Batches API, polling frequently so urgent onboarding jobs usually finish quickly.
[ ] C - Keep both queues on synchronous calls, since batch responses cannot be reliably matched back to submitted documents.
[ ] D - Keep synchronous calls for onboarding forms, and use the Message Batches API for historical contracts with latency-tolerant processing.
