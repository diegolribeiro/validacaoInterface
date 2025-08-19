from enum import Enum

class Campos_interface(Enum):
    CODIGO_LOCAL_ESTOQUE = (0,True,True,True,r'^[ -ü|–]{1,20}$')
    DESCRICAO_LOCAL_ESTOQUE = (1,True,True,False,r'^[ -ü|–]{1,40}$')
    LOCAL_ESTOQUE_GRUPO1 = (2,True,True,False,r'^[ -ü|–]{1,40}$')
    LOCAL_ESTOQUE_GRUPO2 = (3,True,True,False,r'^[ -ü|–]{1,40}$')
    LOCAL_ESTOQUE_GRUPO3 = (4,True,False,False,r'^[ -ü|–]{1,40}$')
    LOCAL_ESTOQUE_GRUPO4 = (5,True,False,False,r'^[ -ü|–]{1,40}$')
    VASO_COMUNICANTE	 = (6,False,True,False,r'^[0-1]{1}$')
    PADRAO_FREQUENCIA	 = (7,True,True,False,r'^[ -ü|–]{1,15}$')
    CAPACIDADE_MAXIMA	 = (8,False,True,False,r'^\d{1,6}(\.\d{1,3})?$')
    OBSERVACAO = (9,True,False,False,r'^[ -ü|–\n\r]{0,200}$')
    CALCULA_DBM	 = (10,False,True,False,r'^[0-1]{1}$')
    CODIGO_TIPO	 = (11,False,False,False,r'^(-1|\d{0,9})$')
    LOCAL_ESTOQUE_GRUPO5 = (12,True,False,False,r'^[ -ü|–]{0,40}$')
    LOCAL_ESTOQUE_GRUPO6 = (13,True,False,False,r'^[ -ü|–]{0,40}$')
    LOCAL_ESTOQUE_GRUPO7 = (14,True,False,False,r'^[ -ü|–]{0,40}$')
    LOCAL_ESTOQUE_GRUPO8 = (15,True,False,False,r'^[ -ü|–]{0,40}$')
    LOCAL_ESTOQUE_GRUPO9 = (16,True,False,False,r'^[ -ü|–]{0,40}$')
    LOCAL_ESTOQUE_GRUP10 = (17,True,False,False,r'^[ -ü|–]{0,40}$')
    LOCAL_ESTOQUE_GRUP11 = (18,True,False,False,r'^[ -ü|–]{0,40}$')
    LOCAL_ESTOQUE_GRUP12 = (19,True,False,False,r'^[ -ü|–]{0,40}$')
    
    

    def __init__(self, indice, campo_string, obrigatorio, chave_primaria, expressao_regular):
        self.indice = indice
        self.campo_string = campo_string
        self.obrigatorio = obrigatorio
        self.chave_primaria = chave_primaria
        self.expressa_regular = expressao_regular