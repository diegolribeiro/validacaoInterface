import streamlit as st
import pandas as pd
import prompt.texto_prompt as texto_prompt
from validador import validador
from langchain.globals import set_debug
import regras_negocio.interface_item_regras as regras_negocio
from langchain.callbacks import get_openai_callback
from langchain_experimental.agents import create_pandas_dataframe_agent

set_debug(False)

def cria_checkbox(checkboxes, valor_inicial, valor_final, campos_interface, campos_checked):
    for campo in campos_interface:
         if campo.indice > valor_inicial and campo.indice <= valor_final:
            checkboxes[campo.name] = st.checkbox(campo.name,value=(True if campo.indice <=campos_checked else False), key=f'checkbox_{campos_interface.__class__.__name__}_{campo.name}')


def monta_tab_interface(llm, cabecalho, df_csv, interface, interface_enum, campos_checked, validacoes_especificas):
    validacao_campos = []
    checkboxes = {}
    st.header(cabecalho) 
        
    col1_campos, col2_campos, col3_campos, col4_campos, col5_campos, col6_campos = st.columns(6)
    df = df_csv

    if df is not None:
         with st.expander("Visualização dos dados", expanded=False, icon=None, width="stretch"):
            st.dataframe(df)
    
    with col1_campos:
        cria_checkbox(checkboxes, -1, 4, interface_enum, campos_checked)
    
    with col2_campos:
        cria_checkbox(checkboxes, 4, 9, interface_enum, campos_checked)

    with col3_campos:
        cria_checkbox(checkboxes, 9, 14, interface_enum, campos_checked) 

    with col4_campos:
        cria_checkbox(checkboxes, 14, 19, interface_enum, campos_checked)

    with col5_campos:
        cria_checkbox(checkboxes, 19, 24, interface_enum, campos_checked)

    with col6_campos:
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

                        validacao_campos.append({"campo" : campo.name, "validacao" : validacao_campos_aux})
                        st.session_state['validacao_execuctada'] = True


        resumo_validacao = """ 
            # Validação geral da interface de item***

            """
        resumo_validacao_especifica = """ 
            # Validação especiespecífica da interface de item

            """
    
    col1_validacao_geral, col2_validacao_especifica, col3_resumo_cliente = st.columns(3)

    with col1_validacao_geral:               
        with st.container(height=500):
            st.markdown(f"***Validação Geral da interface de item***")    
            for campo in validacao_campos:
                st.markdown(f"***{campo['campo']}***")
                resumo_validacao = resumo_validacao + "\n" +f" **Campo:** {campo['campo']}"+ "\n"
                            
                for validacao in campo['validacao']:
                    if validacao['erros_encontrados'] == True:
                        linhas = regras_negocio.lista_para_string(validacao['linhas'])
                        st.badge(f"***{validacao['tipo_validacao']}: Não OK*** // ***Linha(s):*** {linhas}", icon=":material/error:", color="red")
                                        
                        resumo_validacao = resumo_validacao + "\n" + (f"- {validacao['tipo_validacao']}: Não OK // Linha(s): {linhas}") + "\n"
                    else:
                        st.badge(f"***{validacao['tipo_validacao']}: OK***", icon=":material/check:", color="green")
                        resumo_validacao = resumo_validacao + "\n" + (f"- {validacao['tipo_validacao']}: OK") + "\n"
    
    
    
    with col2_validacao_especifica:
        with st.container(height=500):
            st.markdown(f"***Validação Específica da interface de item***")
            valor = st.session_state.get('validacao_execuctada', False)
            if valor:
                for campo in validacoes_especificas:
                    st.markdown(f"***{campo['campo']}***")
                    resumo_validacao_especifica = resumo_validacao_especifica + "\n" +f" **Campo:** {campo['campo']}"+ "\n"
                    # st.write(campo['validacao'])
                    for validacao in campo['validacao']:
                        if validacao['erros_encontrados'] == True:
                            st.badge(f"***{validacao['tipo_validacao']}: Não OK*** // ***Linha(s):*** {validacao['linhas']}", icon=":material/error:", color="red")
                            resumo_validacao_especifica = resumo_validacao_especifica + "\n" + (f"- {validacao['tipo_validacao']}: Não OK // Linha(s): {validacao['linhas']}") + "\n"
                        else:
                            st.badge(f"***{validacao['tipo_validacao']}: OK***", icon=":material/check:", color="green")
                            resumo_validacao_especifica = resumo_validacao_especifica + "\n" + (f"- {validacao['tipo_validacao']}: OK") + "\n"

    
    with col3_resumo_cliente:
        with st.container(height=500):
            st.markdown(f"***Resumo para encaminhar para o cliente***")
            if  st.session_state.get('validacao_execuctada',False):
                modelo_do_prompt = texto_prompt.texto_gerar_resumo_validacao(interface, resumo_validacao)
                prompt = modelo_do_prompt.format(interface=interface)
                #resposta = llm.invoke(prompt)
                st.markdown('resposta.content')
        
               

    
    agent = create_pandas_dataframe_agent(llm, 
                                          df, 
                                          verbose=True, 
                                          agent_type="tool-calling",
                                          prefix=texto_prompt.texto_csv_prompt_prefixo(),
                                          suffix=texto_prompt.texto_csv_prompt_sufixo(),
                                          allow_dangerous_code=True)
                                          #suffix=CSV_PROMPT_SUFFIX)   
    prompt = None
    prompt = st.text_area("Converse com os dados:", key=f'text_area_{interface}')
            
    if st.button("Generate", key=f'button_llm_{interface}'):        
        if prompt:
            with st.spinner("Generating response..."):
                resposta = agent.invoke(prompt, verbose=False)
                st.markdown(resposta['output'])