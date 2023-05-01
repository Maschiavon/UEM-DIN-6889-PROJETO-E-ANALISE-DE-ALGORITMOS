# 12. Projete um algoritmo que encontre o valor máximo de uma Lista não vazia, semelhante ao exercício
# anterior, mas agora a entrada é uma Lista e não uma Lista1. (Dica: assuma que a lista não pode ser
# None e mude o caso base).
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

# Encontra o valor maximo de uma
# Lista não vazia / None =0
def lst_max_val(lst: Lista, maior = 0) -> int:
    if lst is None:
        return maior
    else:
        if maior < lst.primeiro:
            maior = lst.primeiro
            return lst_max_val(lst.resto,maior)
        else:
            return lst_max_val(lst.resto,maior)

assert lst_max_val(Link(20, None)) == 20
assert lst_max_val(Link(15, Link(20, None))) == 20
assert lst_max_val(Link(25, Link(20, Link(40, None)))) == 40