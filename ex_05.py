from typing import List

def calcular_desvio_padrao(valores: List[float]) -> float:
    media = sum(valores) / len(valores)
    variancia = sum((x - media) ** 2 for x in valores) / len(valores)        # usar o for para utilizar os valores da lista
    return variancia ** 0.5

valores = [7,9,10,11,13]

desvio = calcular_desvio_padrao(valores)

print(desvio)