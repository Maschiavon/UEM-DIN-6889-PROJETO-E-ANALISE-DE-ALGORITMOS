# 5. Projete um algoritmo que receba como entrada uma Lista lst e um elemento a e devolva uma Lista
# que é como lst mas com a no final.
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

# Recebe uma lista lst e um elemento a
# e devolve a lista com a no final
def lst_add_a(lst: Lista, a: int) -> Lista:
    if lst is None:
        return Lista(a, None)
    else:
        return Lista(lst.primeiro, lst_add_a(lst.resto, a))

assert lst_add_a(None,0) == Link(0,None)
assert lst_add_a(Link(10,None),3) == Link(10,Link(3,None))
assert lst_add_a(Link(3,Link(4,Link(2,None))),2) == Link(2,None)