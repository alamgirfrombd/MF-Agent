# Architecture and implementation boundaries

## Request flow

User interface → agent planner → approved dataset registry → schema/relationship validation → SQL compiler → SQL guard → read-only database principal → result validation → analytics/reporting.

The LLM must not have direct database credentials. It proposes structured plans; deterministic application code validates and executes.

## Dataset activation gate

A dataset can be marked `active` only after all referenced SQL objects and columns are checked against `output/schema_metadata.json`, primary/foreign keys or explicitly approved logical joins are documented, grain is defined, and business formulas are signed off. Draft datasets are non-executable.

## Missing/next modules

1. Registry schema with typed column definitions and explicit join cardinality.
2. SQL compiler that only compiles approved plan objects (not arbitrary model SQL).
3. Registry-based table/column allowlist in SQL guard.
4. Authentication and branch/area/role authorization.
5. OpenAI provider adapter and LLM response schema validation.
6. Golden questions reconciled against known reports.
7. Financial-year and MRA/PKSF formula catalogue approved by business owners.
