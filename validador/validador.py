

import pandas as pd

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
    
    coluna =  pd.to_numeric(df.iloc[:, campo.indice], errors='coerce') 
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
    """
    Retorna uma lista de índices das linhas onde o valor da coluna informada não corresponde à expressão regular.
    Parâmetros:
        df (pd.DataFrame): O DataFrame a ser analisado.
        campo (Campos_interface_item): O campo a ser validado.      
    Retorno:
        dict: Dicionário com o tipo de validação, se erros foram encontrados, as linhas afetadas e uma mensagem detalhada.
    """
    
    valido = df.iloc[:,campo.indice].astype(str).str.match(regex)
    linhas = df.index[~valido].to_list()
    tem_erro_expressao_regular = bool(linhas)  
    return {
        "tipo_validacao": "Validação das quantidade de caracteres ou uso de caracteres não aceitos.",
        "erros_encontrados" : tem_erro_expressao_regular,
        "linhas": linhas,
        "mensagem_erro_detalhada": "Foram identificados problemas: quantidade de caracteres fora do especificado ou uso de caracteres não aceitos."
        }

def validador_nao_numerica(df, campo):
    """
    Retorna uma lista de índices das linhas onde o valor da coluna informada não é numérico.
    
    Parâmetros:
        df (pd.DataFrame): O DataFrame a ser analisado.
        coluna (str): O nome da coluna a ser validada.
    
    Retorno:
        List[int]: Lista de índices das linhas com valor não numérico.
    """
    # Usando pd.to_numeric com errors='coerce' converte não numéricos para NaN
    valores = df.iloc[:, campo.indice].str.replace(',', '.', regex=False).astype(float, errors='ignore')
    
    valores2 = pd.to_numeric(valores, errors='coerce')
    
    # Obtém índices onde o resultado é NaN (ou seja, valor não era numérico)
    linhas = valores2[valores2.isna()].index.tolist()
    tem_erro_valores_nao_numericos = bool(linhas)
    return {
        "tipo_validacao": "Validação de valores não numéricos",
        "erros_encontrados": tem_erro_valores_nao_numericos,
        "linhas": linhas,
        "mensagem_erro_detalhada": "Foram identificados problemas: valores não numéricos."
    } 