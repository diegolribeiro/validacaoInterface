import pandas as pd
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
import streamlit as st 
import layout.interface_item_modelo as layout_item
import layout.interface_fornecedor_modelo as layout_fornecedor
from enumerator.fornecedorEnum import Campo_interface_fornecedor
from enumerator.itemEnum import Campos_interface_item
from regras_negocio import interface_item_regras

st.set_page_config(layout='wide')
st.title("Validador de interface")
st.session_state['validacao_execuctada'] = False
load_dotenv()
pg = st.navigation(["layout/page1.py"],position="sidebar")
pg.run()

llm = ChatOpenAI(model='gpt-3.5-turbo',
    temperature=0.0,
    api_key=os.getenv("OPENAI_API_KEY"))

df_fornecedor = pd.read_csv("./dados/fornecedores.csv", sep=";", thousands=".", decimal=",", encoding="latin1")
interface_fornecedor = 'Fornecedor'

df_item = pd.read_csv("./dados/itens.csv", sep=";", thousands=".", decimal=",", encoding="latin1")
interface_item = 'Item'

tab_fornecedor, tab_item = st.tabs(["Fornecedor","Item"])

with tab_fornecedor:
    validacoes_especificas_interface_fornecedor = []
    layout_fornecedor.monta_tab_interface_fornecedor(llm, 'Interface de Fornecedor', df_fornecedor, interface_fornecedor, Campo_interface_fornecedor, validacoes_especificas_interface_fornecedor)


with tab_item:
        if df_item is not None and  df_fornecedor is not None:
            validacoes_especificas_interface_item = interface_item_regras.validacao_especifica_interface_item(df_item, df_fornecedor, False)
    
        if df_item is not None:
            layout_item.monta_tab_interface_item(llm, 'Interface de Item', df_item, interface_item, Campos_interface_item, validacoes_especificas_interface_item)
    
    