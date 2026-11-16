"""Small DataFrame aggregation helpers; avoid embedding unapproved financial logic."""
def group_sum(dataframe, group_columns: list[str], value_column: str):
    missing = set(group_columns + [value_column]) - set(dataframe.columns)
    if missing:
        raise ValueError(f"Missing columns: {', '.join(sorted(missing))}")
    return dataframe.groupby(group_columns, dropna=False, as_index=False)[value_column].sum()
