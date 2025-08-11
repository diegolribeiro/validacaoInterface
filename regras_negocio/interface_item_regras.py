


def lista_para_string(linhas):
    if (len(linhas) > 10):
        primeiras_linhas = linhas[:10]
        primeiras_linhas = ', '.join(str(linha + 1) for linha in primeiras_linhas)
        primeiras_linhas = primeiras_linhas + ',...'
        return primeiras_linhas
    else:
        return ', '.join(str(linha + 1) for linha in linhas)
    


def validacao_especifica_interface_item(df_item, df_fornecedor, usa_condigo_externo_fornecedor):
    validacao_campos = []
    validacao_campos.append(valida_item_sem_fornecedor(df_item, df_fornecedor, usa_condigo_externo_fornecedor))
    validacao_campos = [{"campo" : 'CODIGO_EXTERNO', "validacao" :  validacao_campos}]
    return validacao_campos


def valida_item_sem_fornecedor(df_item, df_fornecedor, usa_condigo_externo_fornecedor):
    filtro = df_item.iloc[:,5].isin(df_fornecedor.iloc[:,1])
    linhas = df_item.index[~filtro].to_list()
    tem_erro_expressao_regular = bool(linhas)     
    return {
        "tipo_validacao": "Validação se todos os itens possuem fornecedor cadastrado",
        "erros_encontrados" : tem_erro_expressao_regular,
        "linhas": lista_para_string(linhas),
        "mensagem_erro_detalhada": "Foram identificados problemas: Foram informados itens (produtos) que não possuem fornecedor cadastrado no sistema"
        } 
    
