import pandas as pd
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st 

st.title('Validador de Interfaces')
st.set_page_config(layout='wide')
st.session_state['validacao_execuctada'] = False

pages = {
    "Interfaces": [
        st.Page("layout/fornecedor_modelo.py", title="Interface de fornecedor"),
        st.Page("layout/item_modelo.py", title="Interface de item"),
        st.Page("layout/local_estoque_modelo.py", title="Interface de Local de Estoque"),
        st.Page("layout/dimdemanda1_modelo.py", title="Interface de Local de Dimensão de Demanda 1"),
    ]
}

pg = st.navigation(pages)
pg.run()