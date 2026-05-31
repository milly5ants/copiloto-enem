import streamlit as st
from ai import generate_study_plan

st.set_page_config(page_title="Copiloto ENEM")

st.title("🎓 Copiloto ENEM")

hours = st.number_input(
    "Quantas horas você tem hoje?",
    min_value=1,
    max_value=12,
    value=3
)

if st.button("Gerar Plano"):

    with st.spinner("Montando seu plano..."):
        plan = generate_study_plan(hours)

    st.markdown(plan)