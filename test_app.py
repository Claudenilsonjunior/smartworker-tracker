import streamlit as st
import pandas as pd
import sqlite3

st.title("Tudo funcionando!")
st.write("Streamlit:", st.__version__)
st.write("Pandas:", pd.__version__)

# Testar SQLite
conn = sqlite3.connect(":memory:")
st.success("SQLite conectado com sucesso")
conn.close()