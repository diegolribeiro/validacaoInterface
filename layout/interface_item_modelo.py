from layout.layout_util import monta_tab_interface

def monta_tab_interface_item(llm, cabecalho, df_csv, interface, interface_enum, validacoes_especificas_interface_item):
   campos_checked = 9
   monta_tab_interface(llm, cabecalho, df_csv, interface, interface_enum, campos_checked, validacoes_especificas_interface_item)
   