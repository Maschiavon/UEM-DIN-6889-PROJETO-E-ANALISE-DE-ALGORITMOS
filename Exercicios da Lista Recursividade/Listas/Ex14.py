# 14. Projete um algoritmo que receba como entrada uma Lista de números e devolva uma lista com os
# mesmos valores de entrada mas em ordem não decrescente. (Aplique a ideia que estamos utilizando,
# não tente implementar um método de ordenação específico). Dica: combine o resultado da recursão
# natural com o primeiro elemento usando a função que insere ordenado.
from dataclasses import dataclass
from typing import Union

@dataclass
class Link:
    primeiro: int
    resto: 'Lista'

    def _repr_(self):
        return f'Link({self.primeiro},{self.resto})'

# Uma Lista é um dos valores:
# - None
# - Link(int, Lista)
Lista = Union[None, Link]
#Exemplos
x: Lista = None
y: Lista = Link(10, None)
z: Lista = Link(20, Link(4, None))

# Conta a quantidade de elementos dentro
# de uma Lista lst e retorna o numero
def contar(lst: Lista) -> int:
    if lst is None:
        return 0
    else:
        return contar(lst.resto) + 1

# Recebe uma Lista lst ordenada e um inteiro n
# e devolve a lst com n inserido de forma ordenada
def inserir_ordenado(lst: Lista, n: int) -> Lista:
    if lst is None:
        return Link(n, None)
    else:
        if n < lst.primeiro:
            return Link(n, lst)
        else:
            return Link(lst.primeiro, inserir_ordenado(lst.resto,n))

# Recebe uma Lista lst e retorna lst ordenada
def ordenar_lst(lst: Lista) -> Lista:
    if contar(lst) <= 1:
        return lst
    else:
        if lst.primeiro < lst.resto.primeiro:
            return Link(lst.primeiro, ordenar_lst(lst.resto))
        else:
            return ordenar_lst(inserir_ordenado(lst.resto, lst.primeiro))

assert ordenar_lst(None) == None
assert ordenar_lst(Link(1, None)) == Link(1, None)
assert ordenar_lst(Link(20, Link(30, Link(40, None)))) == Link(20, Link(30, Link(40, None)))
assert ordenar_lst(Link(70, Link(60, Link(80, None)))) == Link(60, Link(70, Link(80, None)))