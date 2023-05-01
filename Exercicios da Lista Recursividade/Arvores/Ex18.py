# 18. Uma árvore binária é de busca se cada nó x da árvore tem as seguintes propriedades:
# • O valor armazenado em x é maior os igual à todos os valores armazenados nos nós da árvore a
# esquerda; e
# • O valor armazenado em x é menor ou igual à todos os valores armazenados nos nós da árvore a
# direita
# Projete um algoritmo que receba como entrada uma árvore binária de busca e um valor e verifique se
# o valor aparece na árvore.
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
#Exemplos
x: Arvore_Binaria = None
y: Arvore_Binaria = Link(None, 10, None)
z: Arvore_Binaria = Link(None, 20, Link(None, 4, None))

# Recebe uma arvore binaria de busca e um valor
# e devolve true se o valor está nessa arvore
def find_val_abb(arv: Arvore_Binaria, a: int) -> bool:
    if arv is None:
        return False
    else:
        if arv.valor == a:
            return True
        if arv.valor > a:
            return find_val_abb(arv.esq, a)
        else:
            return find_val_abb(arv.dir, a)

assert find_val_abb(None,0) == False
assert find_val_abb(Link(None, 5, None), 0) == False
assert find_val_abb(Link(None, 5, None), 5) == True
assert find_val_abb(Link(None, 5, Link(Link(None, 6, None), 7, None)), 9) == False
assert find_val_abb(Link(None, 10, Link(Link(None, 15, None), 20, None)), 15) == True
