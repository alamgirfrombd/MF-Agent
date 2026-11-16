"""Starter Streamlit UI. Database querying remains disabled for draft registries."""
import streamlit as st
from agent.orchestrator import available_datasets

st.set_page_config(page_title="MF Agent", page_icon="📊", layout="wide")
st.title("Microfinance AI Data Agent")
st.caption("Schema-aware analytics assistant — infrastructure setup")
try:
    datasets = available_datasets()
    st.subheader("Dataset Registry Status")
    st.dataframe(datasets, use_container_width=True, hide_index=True)
    st.info("All supplied datasets are currently draft. Verify SQL Server schema and business rules before enabling execution.")
except Exception as exc:
    st.error(f"Registry loading failed: {exc}")
