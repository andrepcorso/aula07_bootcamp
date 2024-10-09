# Filtrar valores maiores que o limite

from typing import List

def filtrar_acima_de(valores: List[float], limite:float) -> float:
    resultado = []
    for valor in valores:    #usar o for para utilizar os valores da lista
        if valor > limite:
            resultado.append(valor)
    return resultado

valores = (5, 4, 2, 1)
limite = 3


filtro = filtrar_acima_de(valores,limite)

print(filtro)
