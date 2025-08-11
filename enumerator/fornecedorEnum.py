from enum import Enum


class Campo_interface_fornecedor(Enum):
    DESCRICAO_FORNECEDOR = (0,True,True,True,r'^[ -ü|–\n\r]{1,100}$')
    CODIGO_FORNECEDOR = (1,True,True,False,r'^[ -ü|–]{0,100}$')
    GRUPO1_FORNECEDOR = (2,True,False,False,r'^[ -ü|–]{0,40}$')
    GRUPO2_FORNECEDOR = (3,True,False,False,r'^[ -ü|–]{0,40}$')
    CONTATO = (4,True,False,True,r'^[ -ü|–]{0,40}$')
    EMAIL = (5,True,False,True,r'^[ -ü|–]{0,40}$')
    FREQUENCIA_ANALISE = (6,True,False,False,r'^[ -ü|–]{0,15}$')
    INTEGRACAO_EXTERNA = (7,False,False,False,r'[0-1]{0,1}')
    TIPO_FATURAMENTO = (8,False,False,False,r'^(-1|\d{0,9})$')
    VALOR_FATURAMENTO_MINIMO = (9,False,True,False,r'^\d{0,7}(\.\d{1,2})?$')
    HORIZONTE_MAXIMO_ANTECIPACAO = (10,False,False,False,r'^\d{0,3}$')
    TRAVA_FATURAMENTO_MAXIMO = (11,False,True,False,r'^\d{0,8}(\.\d{1,2})?$')
    PERCENTUAL_MINIMO_ANTECIPAÇÃO = (12,False,False,False,r'^\d{0,2}$')
    CRITERIO_PRIORIZACAO = (13,False,False,False,r'[0-1]{0,1}')
    HABILITA_FATURAMENTO_MINIMO	= (14,False,False,False,r'^\d{0,1}$')
    CLASSE	= (15,True,False,False,r'^[ -ü|–]{0,9}$')
    CRITERIO_FATURAMENTO_MINIMO	= (16,False,False,False,r'^\d{0,1}$')

    def __init__(self, indice, campo_string, obrigatorio, chave_primaria, expressao_regular):
        self.indice = indice
        self.campo_string = campo_string
        self.obrigatorio = obrigatorio
        self.chave_primaria = chave_primaria
        self.expressa_regular = expressao_regular