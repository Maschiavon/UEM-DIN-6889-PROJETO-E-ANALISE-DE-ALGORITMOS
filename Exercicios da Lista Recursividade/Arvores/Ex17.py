# 17. Projete um algoritmo que receba como entrada uma árvore binária e um valor e verifique se o valor
# aparece na árvore (observe que estamos falando apenas de árvores binárias e não de árvores binárias
# de busca, ou seja, não existe nenhum restrição sobre como os valores estão espelhados pela árvore).
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

# Recebe uma arvore binaria e um valor e devolve true se
# o valor está nessa arvore
def find_val(arv: Arvore_Binaria, a: int) -> bool:
    if arv is None:
        return False
    else:
        if arv.valor == a:
            return True
        return find_val(arv.esq, a) or find_val(arv.dir, a)

assert find_val(None,0) == False
assert find_val(Link(None, 5, None), 0) == False
assert find_val(Link(None, 5, None), 5) == True
assert find_val(Link(None, 5, Link(Link(None, 3, None), 4, None)), 1) == False
assert find_val(Link(None, 5, Link(Link(None, 3, None), 4, None)), 3) == True