# Registry guide

The current seven JSON files are starter definitions, not verified mappings. Preserve `status: draft` until the live SQL Server metadata and business definitions are confirmed.

For each logical table, complete: schema-qualified SQL object, verification status, grain, primary key, columns (logical name, SQL name, type, nullable, description), relationships (join keys and cardinality), approved filters, and data classification. For each metric, record a unique ID, formula, aggregation level, date basis, exclusions, and business approver.
