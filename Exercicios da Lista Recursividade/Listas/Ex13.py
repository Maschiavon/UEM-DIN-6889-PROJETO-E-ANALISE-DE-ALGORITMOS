# 13. Projete um algoritmo que receba como entrada uma Lista lst de números em ordem não decrescente
# e um número n e devolva uma Lista com os elementos de lst e com n em ordem não decrescente (ou
# seja, a função insere n na lista ordenada produzindo uma nova lista).
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

assert inserir_ordenado(None, 1) == Link(1, None)
assert inserir_ordenado(Link(1, None), 2) == Link(1, Link(2, None))
assert inserir_ordenado(Link(1, Link(2, None)), 2) == Link(1, Link(2, Link(2, None)))
assert inserir_ordenado(Link(20, Link(30, Link(40, None))), 5) == Link(5, Link(20, Link(30, Link(40, None))))