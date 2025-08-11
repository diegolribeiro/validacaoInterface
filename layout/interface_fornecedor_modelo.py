from layout.layout_util import monta_tab_interface

def monta_tab_interface_fornecedor(llm, cabecalho, df_csv, interface, interface_enum, validacoes_especificas_interface_fornecedor):
   campos_checked = 8
   monta_tab_interface(llm, cabecalho, df_csv, interface, interface_enum, campos_checked, validacoes_especificas_interface_fornecedor)
