import streamlit as st
import plotly.express as px
import os
from database import init_db, add_contact, get_contacts
from analytics import conversion_rates, funnel_dataframe

# DEVE ser a 1ª chamada Streamlit
st.set_page_config(page_title="SmartWorker Tracker",
                  page_icon="📊", layout="wide")

os.makedirs("data", exist_ok=True)
init_db()

with st.sidebar:
  st.header("➕ Novo contato")
  name = st.text_input("Nome")
  # ... demais campos
  if st.button("Adicionar", type="primary"):
    add_contact(name, ...)
    st.rerun()