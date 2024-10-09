# Calcular Média de Valores em uma Lista

from typing import List


def calcular_media(valores: List[float]) -> float:
    return sum(valores)/ len(valores)

valores = (5, 4, 2, 1)

media = calcular_media(valores)

print(media)