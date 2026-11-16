# Security baseline

- Dedicated least-privilege SQL identity; no `db_owner` or `sysadmin`.
- Prefer approved SQL views over direct access to operational tables.
- Enforce branch/area access in the database or a trusted server-side authorization layer; never rely on prompt instructions.
- Parameterize user-provided values; allowlist identifiers from verified registry metadata.
- Limit query duration, returned rows, and result bytes.
- Audit user, timestamp, dataset, normalized query hash, duration, row count, and status; avoid logging member PII or secrets.
- Encrypt database transport and validate server certificates in production.
