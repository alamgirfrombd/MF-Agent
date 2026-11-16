"""Chat UI placeholder; planner integration remains gated by verified registries."""
import streamlit as st
from agent.intent import validate_question

st.subheader("Ask your microfinance data question")
question = st.chat_input("বাংলা বা English-এ প্রশ্ন লিখুন")
if question:
    try:
        clean = validate_question(question)
        st.chat_message("user").write(clean)
        st.warning("AI planning and SQL execution will be enabled after schema and registry verification.")
    except Exception as exc:
        st.error(str(exc))
