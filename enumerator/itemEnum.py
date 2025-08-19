from enum import Enum

class Campos_interface_item(Enum):
    CODIGO_ITEM = (0,True,True,True,r'^[A-Za-z0-9/_/.-]{1,50}$')
    CODIGO_AUXILIAR = (1,True,False,False,r'^[ -ü|–]{0,50}$')
    DESCRICAO_ITEM = (2,True,True,False,r'^[ -ü|–\n\r]{1,300}$')
    UNIDADE = (3,True,True,False,r'^[ ,-;A-zÀ-ü]{1,10}$')
    FATOR_CONVERSAO = (4,False,True,False,r'^\d{1,7}(\,\d{1,6})?$')
    DESCRICA_FORNECEDOR	= (5,True,True,False,r'^[ -ü|–\n\r]{1,100}$')
    DESCRICAO_ITEM_GRUPO_1 = (6,True,True,False,r'^[ -ü|–\n\r]{1,100}$')
    DESCRICAO_ITEM_GRUPO_2 = (7,True,True,False,r'^[ -ü|–\n\r]{1,100}$')
    DESCRICAO_ITEM_GRUPO_3 = (8,True,True,False,r'^[ -ü|–\n\r]{1,100}$')
    DESCRICAO_ITEM_GRUPO_4 = (9,True,True,False,r'^[ -ü|–\n\r]{1,100}$')
    DESCRICAO_ITEM_GRUPO_5 = (10,True,True,False,r'^[ -ü|–\n\r]{1,100}$')
    DESCRICAO_ITEM_GRUPO_6 = (11,True,True,False,r'^[ -ü|–\n\r]{1,100}$')
    FATOR_CONVERSAO_1 = (12,False,True,False,r'^\d{0,7}(\,\d{1,6})?$')
    FATOR_CONVERSAO_2 = (13,False,True,False,r'^\d{0,7}(\,\d{1,6})?$')
    FATOR_CONVERSAO_3 = (14,False,True,False,r'^\d{0,7}(\,\d{1,6})?$')
    DESCRICAO_ITEM_GRUPO_7 = (15,True,True,False,r'^[ -ü|–\n\r]{1,100}$')
    DESCRICAO_ITEM_GRUPO_8 = (16,True,True,False,r'^[ -ü|–\n\r]{1,100}$')
    DESCRICAO_ITEM_GRUPO_9 = (17,True,True,False,r'^[ -ü|–\n\r]{1,100}$')
    DESCRICAO_ITEM_GRUPO_10 = (18,True,True,False,r'^[ -ü|–\n\r]{1,100}$')
    DESCRICAO_ITEM_GRUPO_11 = (19,True,True,False,r'^[ -ü|–\n\r]{1,100}$')
    DESCRICAO_ITEM_GRUPO_12 = (20,True,True,False,r'^[ -ü|–\n\r]{1,100}$')
    URL_IMAGEM = (21,True,False,False,r'^[ -ü|–\n\r]{0,200}$')

    def __init__(self, indice, campo_string, obrigatorio, chave_primaria, expressao_regular):
        self.indice = indice
        self.campo_string = campo_string
        self.obrigatorio = obrigatorio
        self.chave_primaria = chave_primaria
        self.expressa_regular = expressao_regular