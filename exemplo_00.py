valor_1 = 1
valor_2 = 2
valor_4 = 6
valor_5 = 8



def soma(valor_1: float, valor_2: float) -> float:
    resultado_da_soma = valor_1 + valor_2
    return resultado_da_soma

valor_3 = soma(valor_1, valor_2)
valor_6 = soma(valor_4, valor_5)

print(valor_3)

print(valor_6)