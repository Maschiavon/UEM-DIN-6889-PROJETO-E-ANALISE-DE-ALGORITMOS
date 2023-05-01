# 15. Faça a definição de um tipo para representar uma árvore binária. Uma árvore binária ou é vazia, ou
# é um nó com um valor inteiro e uma árvore binária esquerda e uma árvore binária direita.
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

