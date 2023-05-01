# 7. Projete um algoritmo que receba como entrada duas Listas, lst1 e lst2, e devolva uma nova lista
# contendo os elementos de lst1 seguidos dos elementos de lst2. Dica: faça a recursão pensado em
# lst1 e considere lst2 como uma valor atômico (como o parâmetro a dos primeiros exercícios).
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

# Recebe uma lista lst1 e lst2 e
# devolve uma lista com os elementos
# da lst1 seguidos da lst2
def lst_juntar(lst1: Lista, lst2:Lista) -> Lista:
    if lst1 is None:
        return lst_juntar(lst2,None)
    elif lst2 is None:
        return lst1
    else:
        return Lista(lst1.primeiro, lst_juntar(lst1.resto, lst2))

assert lst_juntar(None,None) == None
assert lst_juntar(Link(10,None),Link(11,Link(12,None))) == Link(10, Link(11, Link(12,None)))
assert lst_juntar(Link(3,Link(4,Link(2,None))),None) == Link(3,Link(4,Link(2,None)))