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

# Ver se o elemento v está no meio da lista e
# se não estiver procura nas metades
def busca_binaria(lst: Lista, v:int, a:int, b:int ) -> bool:
    if a == b:
        return False
    else:
        meio = (a+b)//2
        if v == lst[meio]:
            return True
        elif v < lst[meio]:
            return busca_binaria(lst,v,a,meio)
        else:
            return busca_binaria(lst,v,meio+1,b)