# Database schema discovery

Run `python scripts/discover_schema.py` after configuring SQL Server. The export includes table inventory, column metadata, declared primary keys, and declared foreign keys. Legacy MFI databases may have logical joins without declared FK constraints; those must be documented and approved separately. No data-row sampling is performed by the default discovery script.
