# 3. Projete um algoritmo que receba como entrada uma Lista lst e um elemento a e conte quantas vezes
# a aparece em lst.
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

# Conta a quantidade de elementos que são 
# iguais a "a" dentro de uma Lista lst e
# retorna o resultado

def contar_a(lst: Lista, a: int) -> int:
    if lst is None:
        return 0
    else:
        if lst.primeiro == a:
            return contar_a(lst.resto,a) + 1 
        else:
            return contar_a(lst.resto, a)

assert contar_a(None,0) == 0
assert contar_a(Link(10,None),10) == 1
assert contar_a(Link(2,Link(4,Link(2,None))),2) == 2
assert contar_a(Link(3,Link(4,Link(2,Link(8,None)))),8) == 1