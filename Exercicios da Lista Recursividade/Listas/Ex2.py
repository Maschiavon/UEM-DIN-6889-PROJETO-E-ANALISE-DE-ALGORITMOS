# 2. Projete um algoritmo que receba como entrada uma Lista lst e verifique se todos os elementos de lst
# são pares.
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

# Verificar se todos os elementos da lista são pares,
# se sim retorna True caso contrario retorna False
# se a lista for vazia retorna True

def lst_par(lst: Lista) -> bool:
    if lst is None:
        return True
    else:
        if (lst.primeiro % 2) != 0:
            return False
        else:
            return lst_par(lst.resto)
        

assert lst_par(None) == True
assert lst_par(Link(10,None)) == True
assert lst_par(Link(10,Link(3,Link(2,None)))) == False
assert lst_par(Link(8,Link(4,Link(2,Link(0,None))))) == True