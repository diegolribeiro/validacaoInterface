from langchain.prompts import PromptTemplate

def texto_csv_prompt_prefixo():
    return """
    First set the pandas display options to show all the columns,
    get the column names, then answer the question.
    """


def texto_csv_prompt_sufixo():
    CSV_PROMPT_SUFFIX = """
    - **SEMPRE** antes de dar a Resposta Final, tente outro método.
    Em seguida, reflita sobre as respostas dos dois métodos que você usou e pergunte a si mesmo
    se ele responde corretamente à pergunta original.
    Se não tiver certeza, tente outro método.
    
    - Se os métodos testados não derem o mesmo resultado, reflita e
    tente novamente até que você tenha dois métodos com o mesmo resultado.
    - Se ainda assim não conseguir chegar a um resultado consistente, diga que
    não tem certeza da resposta.
    
    - Se tiver certeza da resposta correta, crie uma resposta bonita
    e completa usando Markdown.
    
    - **NÃO INVENTA UMA RESPOSTA NEM USE CONHECIMENTO PRÉVIO,
    USE APENAS OS RESULTADOS DOS CÁLCULOS QUE VOCÊ FEZ**.
    
    - **SEMPRE**, como parte da sua "Resposta Final", explique como você chegou
    à resposta em uma seção que comece com: "\n\nExplicação:\n".
    No Explicação, mencione os nomes das colunas que você usou para chegar
    à resposta final.
    """
    return CSV_PROMPT_SUFFIX


def texto_gerar_resumo_validacao(interface, resumo_validacao):
    return PromptTemplate.from_template("""
    Você é um agente responsável por organizar e comunicar ao cliente os resultados de validações já realizadas em interfaces de dados. Após receber as informações sobre os erros encontrados, sua principal função é estruturar um resumo claro, objetivo e orientativo, detalhando quais problemas foram identificados e quais ações corretivas precisam ser tomadas pelo cliente.

    Funções principais:
    Organizar os dados das validações realizadas, estruturando as mensagens de forma compreensível.
    Comunicar ao cliente, de maneira clara e objetiva, todos os erros ou inconsistências detectados na interface de dados.
    Sugerir ou orientar quais campos, linhas e correções precisam ser efetuadas pelo cliente para solucionar os problemas apontados.
    A resposta tem que ser no formato markdown
                                                                                            
    Objetivo:
    Garantir que o cliente compreenda facilmente os resultados das validações, facilitando a tomada de decisão e a correção rápida dos dados para conformidade com os requisitos esperados.

    Abaixo estão os campos validados da interface de: {interface}, contendo o validação de cada campo.
    """ + resumo_validacao)