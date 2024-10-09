from typing import List

def contar_valores_unicos(lista: List[int]) -> int:
    return len(set(lista))


valores = (5, 4, 2, 1)

unicos = contar_valores_unicos(valores)

print(unicos)