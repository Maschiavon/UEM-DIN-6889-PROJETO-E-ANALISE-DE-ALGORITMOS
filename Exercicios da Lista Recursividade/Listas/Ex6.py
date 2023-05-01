# 6.Projete um algoritmo que receba como entrada uma Lista lst e devolva uma Lista com os mesmos
# elementos de lst mas em ordem reversa. Dica: combine o resultado da recursão natural com o primeiro
# elemento usando a função que insere no final.
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

#Insere o elemento "a" no final da lista
def Inserir_Final(lst: Lista, a:int) -> Lista:
    if lst is None:
        return Link(a, None)
    else:
        return Link(lst.primeiro, Inserir_Final(lst.resto, a))

assert Inserir_Final(None, 3) == Link(3,None)
assert Inserir_Final(Link(4,None), 3) == Link(4,Link(3,None))
assert Inserir_Final(Link(3, Link(4,None)), 7) == Link(3,Link(4,Link(7, None)))

# Recebe uma lista lst devolve a
# lista invertida
def lst_reversa(lst: Lista) -> Lista:
    if lst is None:
        return None
    else:
        return Inserir_Final( lst_reversa(lst.resto), lst.primeiro)

assert lst_reversa(None) == None
assert lst_reversa(Link(10,None)) == Link(10,None)
assert lst_reversa(Link(3,Link(4,Link(2,None)))) == Link(2,Link(4,Link(3,None)))