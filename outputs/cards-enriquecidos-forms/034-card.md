Scenario: Your extraction system parses e-commerce product descriptions to extract specifications like dimensions, weight, and materials into JSON. Despite having a well-defined schema, the model inconsistently extracts the "materials" field—sometimes returning "cotton blend", other times "Cotton/Polyester mix", and occasionally omitting the field when material information is clearly present in the source. What's the most effective way to improve extraction consistency?

---

[ ] A - Make the "materials" field required instead of optional in the schema to force the model to always extract a valueB.Switch to a more capable model tier since inconsistent extraction indicates insufficient model capabilityC.Set temperature to 0 to eliminate randomness and ensure deterministic outputsD.Add few-shot examples showing 2-3 complete input-output pairs with standardized material description formats
[ ] B - Switch to a more capable model tier since inconsistent extraction indicates insufficient model capabilityC.Set temperature to 0 to eliminate randomness and ensure deterministic outputsD.Add few-shot examples showing 2-3 complete input-output pairs with standardized material description formats
[ ] C - Set temperature to 0 to eliminate randomness and ensure deterministic outputsD.Add few-shot examples showing 2-3 complete input-output pairs with standardized material description formats
[ ] D - Add few-shot examples showing 2-3 complete input-output pairs with standardized material description formats
