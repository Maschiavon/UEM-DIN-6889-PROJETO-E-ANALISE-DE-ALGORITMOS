# 4. Projete um algoritmo que receba como entrada uma Lista lst e um elemento a e devolva uma Lista
# que é como lst mas sem as ocorrências dos valores maiores que a.
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

# Compara a quantidade de elementos
# de uma Lista lst e remove todos que são
# maiores que "a" e devolve a lista nova
def remover_maior_que_a(lst: Lista, a: int) -> Lista:
    if lst is None:
        return None
    else:
        if lst.primeiro > a:
            return remover_maior_que_a(lst.resto,a)
        else:
            return Lista(lst.primeiro, remover_maior_que_a(lst.resto, a))

assert remover_maior_que_a(None,0) == None
assert remover_maior_que_a(Link(10,None),10) == Link(10,None)
assert remover_maior_que_a(Link(3,Link(4,Link(2,None))),2) == Link(2,None)