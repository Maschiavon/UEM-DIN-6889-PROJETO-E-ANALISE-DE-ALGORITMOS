# 1. Projete um algoritmo que receba como entrada uma Lista lst e conte quantos elementos lst tem.
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
z: Lista = Link(20, Link(4,None))

# Conta a quantidade de elementos dentro
# de uma Lista lst e retorna o numero
def contar(lst: Lista) -> int:
    if lst is None:
        return 0
    else:
        #lst é um Link
        return contar(lst.resto) + 1

assert contar(None) == 0
assert contar(Link(10,None)) == 1
assert contar(Link(10,Link(4,Link(2,None)))) == 3

print(contar(Link(10,None)))