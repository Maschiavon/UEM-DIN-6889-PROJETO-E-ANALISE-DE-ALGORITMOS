# 2. Projete um algoritmo que verifique se os elementos de um arranjo estão em ordem não decrescente.
from dataclasses import dataclass
from typing import Union


# Recebe um arranjo e verifica se
# a ordem está em não descrescente
def verifica_ordem(lista: list, a=1) -> bool:
    if len(lista) <= 1 or len(lista) == a or list is None:
        return True
    else:
        if lista[a] < lista[a - 1]:
            return False
        else:
            return verifica_ordem(lista, a + 1)


lista0 = []
lista1 = [1]
lista2 = [1, 5, 2, 6]
lista3 = [1, 2, 3, 4, 5]
lista4 = [1, 2, 3, 4, 5, 6, 1]

print(verifica_ordem(lista0))
print(verifica_ordem(lista1))
print(verifica_ordem(lista2))
print(verifica_ordem(lista3))
print(verifica_ordem(lista4))