import streamlit as st
from  enumerator.fornecedorEnum import Campo_interface_fornecedor as interface_enum
from layout.layout_util import cria_checkboxes_por_coluna, exibe_validacao_geral, exibe_validacao_especifica
from regras_negocio import LLM as llm
from validador import validador
import pandas as pd
import prompt.texto_prompt as texto_prompt


df = pd.read_csv("./dados/fornecedores.csv", sep=";", thousands=".", decimal=",", encoding="latin1", keep_default_na=False, dtype=str)
interface = 'Interface de Fornecedor'
st.title(interface)
col1_campos, col2_campos, col3_campos, col4_campos, col5_campos, col6_btn_validar = st.columns(6)

validacao_campos = []
checkboxes = {}

resumo_validacao = ""

with col1_campos: 
   cria_checkboxes_por_coluna(checkboxes,-1,4,interface_enum,11)

with col2_campos:
   cria_checkboxes_por_coluna(checkboxes,4,9,interface_enum,11)

with col3_campos:
   cria_checkboxes_por_coluna(checkboxes,9,14,interface_enum,11)

with col4_campos:
   cria_checkboxes_por_coluna(checkboxes,14,19,interface_enum,11)

with col5_campos:
   cria_checkboxes_por_coluna(checkboxes,19,24,interface_enum,11)


with col6_btn_validar:
   if st.button(f'Validar {interface}', icon=':material/list_alt_check:'):
      with st.spinner("Validando os dados...",show_time=True):
         for campo in interface_enum:
                    
            validacao_campos_aux = []
            valida_interface = checkboxes[campo.name]
         
            if valida_interface:
               validacao_campos_aux.append(validador.indices_invalidos_regex(df, campo, campo.expressa_regular))

               if campo.chave_primaria:
                  validacao_campos_aux.append(validador.validador_coluna_valores_duplicados(df, campo))

               if campo.obrigatorio:
                  validacao_campos_aux.append(validador.validador_coluna_valor_nulo(df, campo))
                        
               if not campo.campo_string:
                  validacao_campos_aux.append(validador.validador_coluna_valor_negativo(df, campo))
                  validacao_campos_aux.append(validador.validador_nao_numerica(df, campo))

               validacao_campos.append({"campo" : campo.name, "validacao" : validacao_campos_aux})
               st.session_state['resposta_validacao_especifica_item'] = False
               st.session_state.validacao_executada = True

if df is not None:
   with st.expander("Visualização dos dados", expanded=False, icon=None, width="stretch"):
      st.dataframe(df)

col1_validacao_geral, col2_validacao_especifica, col3_resumo_cliente = st.columns(3)
with col1_validacao_geral:               
   with st.container(height=500):
      st.markdown(f"***Validação Geral da {interface}***")
      resumo_validacao = exibe_validacao_geral(validacao_campos)

with col2_validacao_especifica:               
   with st.container(height=500):
      st.markdown(f"***Validação Específica da {interface}***")
      
         
           

with col3_resumo_cliente:
   with st.container(height=500):
      st.markdown(f"***Resumo para encaminhar para o cliente***")
      
      if st.session_state.get("validacao_executada",False):
         modelo_do_prompt = texto_prompt.texto_gerar_resumo_validacao(interface, resumo_validacao)
         prompt = modelo_do_prompt.format(interface=interface)
         #llm = llm.llm()
         #st.session_state.resposta_llm_fornecedor = llm.invoke(prompt).content
      
      st.markdown(st.session_state.get('resposta_llm_fornecedor',''))
      st.session_state.validacao_executada = False
         
         