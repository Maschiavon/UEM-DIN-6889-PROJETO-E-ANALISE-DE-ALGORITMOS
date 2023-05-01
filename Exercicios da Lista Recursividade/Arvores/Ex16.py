# 16. Projete um algoritmo que receba como entrada uma árvore binária e conte a quantidade de nós na
# árvore.
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


# Recebe uma arvore binaria e devolve qtd de nós
# dessa arvore
def count_no(arv: Arvore_Binaria) -> int:
    if arv is None:
        return 0
    else:
        return count_no(arv.esq) + count_no(arv.dir) + 1

assert count_no(None) == 0
assert count_no(Link(None, 5, None)) == 1
assert count_no(Link(None, 5, Link(Link(None, 3, None), 4, None))) == 3
