# 9. Projete um algoritmo que verifique se os elementos de uma Lista estão em ordem não decrescente
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

# Recebe uma lista e verifica se a ela
# está em ordem não decrescente
def verfica_ordem(lst1: Lista) -> Lista:
    if contar(lst1) <= 1:
        return True
    else:
        if lst1.primeiro < lst1.resto.primeiro:
            return verfica_ordem(lst1.resto)
        else:
            return False

assert verfica_ordem(None) == True
assert verfica_ordem(Link(10,None)) == True
assert verfica_ordem(Link(4,Link(3,Link(2,None)))) == False
assert verfica_ordem(Link(2,Link(4,Link(2,None)))) == False