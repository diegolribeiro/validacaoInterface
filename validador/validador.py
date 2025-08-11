

def validador_coluna_valor_nulo(df, campo):

    coluna = df.iloc[:, campo.indice]
    tem_nulos = coluna.isnull().any()
    linhas_valor_nulo = coluna[coluna.isnull()].index.tolist()
    return {
        "tipo_validacao": "Validação Valor nulo",
        "erros_encontrados": tem_nulos,
        "linhas": linhas_valor_nulo
    }

def validador_coluna_valor_negativo(df, campo):

    coluna = df.iloc[:, campo.indice]
    tem_negativos =  (coluna < 0).any()
    linhas_valor_negativo = coluna[coluna < 0].index.tolist()
    return {  
        "tipo_validacao": "Validação Valor negativo",
        "erros_encontrados": tem_negativos,
        "linhas": linhas_valor_negativo,
        "mensagem_erro_detalhada": "O campo não pode possuir valor negativo."
    }

def validador_coluna_valores_duplicados(df, campo):

    coluna = df.iloc[:, campo.indice]
    duplicados = coluna.duplicated(keep='first')
    tem_valores_repetidos = duplicados.any()
    linha_valores_repetidos = coluna[duplicados].index.tolist()
    return {
        "tipo_validacao": "Validação Valores repetidos",
        "erros_encontrados": tem_valores_repetidos,
        "linhas": linha_valores_repetidos,
        "mensagem_erro_detalhada": "O campo não pode possuir valores repetidos."
    }

def indices_invalidos_regex(df, campo, regex):
    valido = df.iloc[:,campo.indice].astype(str).str.match(regex)
    linhas = df.index[~valido].to_list()
    tem_erro_expressao_regular = bool(linhas)  
    return {
        "tipo_validacao": "Validação das quantidade de caracteres ou uso de caracteres não aceitos.",
        "erros_encontrados" : tem_erro_expressao_regular,
        "linhas": linhas,
        "mensagem_erro_detalhada": "Foram identificados problemas: quantidade de caracteres fora do especificado ou uso de caracteres não aceitos."
        } 