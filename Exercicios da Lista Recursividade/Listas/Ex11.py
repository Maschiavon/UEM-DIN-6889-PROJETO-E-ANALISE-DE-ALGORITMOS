# 11. Projete um algoritmo que encontre o valor máximo de uma Lista1. (Em Python você pode verificar se
# um valor é de um tipo específico usando isinstance, por exemplo, para verificar se a é do tipo int,
# use isinstance(a, int))
from dataclasses import dataclass
from typing import Union

@dataclass
class Link:
    primeiro: int
    resto: 'Lista'

    def _repr_(self):
        return f'Link({self.primeiro},{self.resto})'

@dataclass
class Link1:
    primeiro: int
    resto: 'Lista1'

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

# Uma Lista1 é um dos valores:
# - int
# - Link(int, Lista1)
Lista1 = Union[int, Link1]
x1: Lista1 = 1
y1: Lista1 = Link1(20, 3)
z1: Lista1 = Link1(40, Link1(50,6))

# Conta a quantidade de elementos dentro
# de uma Lista lst e retorna o numero
def contar1(lst: Lista1) -> int:
    if isinstance(lst, int):
        return 1
    else:
        return contar1(lst.resto) + 1

# Recebe uma Lista 1 e devolve seu valor maximo
# isinstance(a, int)
def lst1_max_val(lst1: Lista1, maior=0) -> int:
    if contar1(lst1) == 1:
        if lst1<maior:
            return maior
        return lst1
    else:
        if maior < lst1.primeiro:
            maior = lst1.primeiro
            return lst1_max_val(lst1.resto,maior)
        else:
            return lst1_max_val(lst1.resto,maior)

assert lst1_max_val(1) == 1
assert lst1_max_val(Link1(20, 3)) == 20
assert lst1_max_val(Link1(15, Link1(20, 3))) == 20