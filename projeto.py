import csv

path_arquivo = "vendas.csv"

def ler_csv(nome_do_arquivo_csv:str) -> list[dict]:
    """
    Função que lê um arquivo csv e retorna uma lista de dicionários
    """
    lista =[]
    with open(nome_do_arquivo_csv, mode="r", encoding="utf-8")  as arquivo: #With serve para abrir o arquivo
        leitor = csv.DictReader(arquivo)
        for linha in leitor:                       #utilizar o for para inserir as linhas dentro da lista
            lista.append(linha)
    return lista

def filtrar_produtos_nao_entregues(lista:list[dict]) -> int:
    """
    Função que filtra produtos que não foram entregues, mostrando somente produtos que foram entregues
    """
    lista_com_produtos_filtrados =[]
    for produto in lista:
        if produto.get("entregue") == "True":
            lista_com_produtos_filtrados.append(produto)
    return lista_com_produtos_filtrados

def somar_valores_dos_produtos(lista_com_produtos_filtrados:list[dict]) -> list[dict]:
    """
    Função que soma os valores dos produtos entregues
    """
    valor_total = 0
    for produto in lista_com_produtos_filtrados:
        valor_total += int(produto.get("price"))
    return valor_total

