# 19. Projete um algoritmo que verifique se um árvore binária é de busca.
from dataclasses import dataclass
from typing import Union


@dataclass
class Link:
    esq: 'Lista'
    valor: int
    dir: 'Lista'

    def _repr_(self):
        return f'Link({self.esq},{self.valor},{self.dir})'


# Uma Arvore_Binaria é um dos valores:
# - None
# - Link(Arvore_Binaria, int, Arvore_Binaria)
Arvore_Binaria = Union[None, Link]
# Exemplos
x: Arvore_Binaria = None
y: Arvore_Binaria = Link(None, 10, None)
z: Arvore_Binaria = Link(None, 20, Link(None, 4, None))

# Recebe uma arvore binaria e devolve o
# valor do no
def valor_no(arv: Arvore_Binaria) -> int:
    if arv is None:
        return 0
    else:
        return arv.valor

def valor_no2(arv: Arvore_Binaria) -> int:
    if arv is None:
        return 999999999
    else:
        return arv.valor

# Recebe uma arvore binaria de busca e um valor
# e devolve true se o valor está nessa arvore
def verifica_abb(arv: Arvore_Binaria) -> bool:
    if arv is None:
        return True
    else:
        if valor_no2(arv.dir) > arv.valor > valor_no(arv.esq):
            return verifica_abb(arv.dir) and verifica_abb(arv.esq)
        else:
            return False

assert verifica_abb(None) == True
assert verifica_abb(Link(None, 5, None)) == True
assert verifica_abb(Link(None, 5, Link(None, 4, None))) == False
assert verifica_abb(Link(None, 5, Link(Link(None, 6, None), 7, None))) == True
assert verifica_abb(Link(None, 10, Link(Link(None, 15, None), 20, None))) == True