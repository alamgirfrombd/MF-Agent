import pytest
pytest.importorskip("sqlglot")
from sql_engine.sql_guard import validate_read_only_sql, SQLRejected

def test_select_allowed():
    assert "SELECT" in validate_read_only_sql("SELECT TOP 5 * FROM dbo.LoanData")

@pytest.mark.parametrize("sql", [
    "DELETE FROM dbo.LoanData",
    "UPDATE dbo.LoanData SET Amount=0",
    "DROP TABLE dbo.LoanData",
    "SELECT * INTO dbo.CopyTable FROM dbo.LoanData",
    "SELECT 1; DELETE FROM dbo.LoanData",
])
def test_write_sql_rejected(sql):
    with pytest.raises(SQLRejected):
        validate_read_only_sql(sql)
