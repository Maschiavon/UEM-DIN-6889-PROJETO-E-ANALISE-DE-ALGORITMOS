# 8.Projete um algoritmo que receba como entrada uma Lista lst e devolva uma Lista que é como lst
# mas com apenas uma ocorrência dos elementos repetidos consecutivos. Por exemplos, se lst for
# ⟨3, 3, 3, 1, 5, 5, 1, 1, 1⟩ a saída deve ser ⟨3, 1, 5, 1⟩.
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

# Conta a quantidade de elementos que são
# iguais a "a" dentro de uma Lista lst e
# retorna o resultado
def contar_a(lst: Lista, a: int) -> int:
    if lst is None:
        return 0
    else:
        if lst.primeiro == a:
            return contar_a(lst.resto,a) + 1
        else:
            return contar_a(lst.resto, a)

# Recebe uma lista lst1 e devolve
# uma lista com os elementos de ls1
# sem repetição
def lst_sem_rep(lst1: Lista) -> Lista:
    if contar(lst1) <= 1:
        return lst1
    else:
        if contar_a(lst1,lst1.primeiro) > 1:
            return lst_sem_rep(lst1.resto)
        else:
            return Link(lst1.primeiro ,lst_sem_rep(lst1.resto))

assert lst_sem_rep(None) == None
assert lst_sem_rep(Link(10,None)) == Link(10, None)
assert lst_sem_rep(Link(4,Link(4,Link(2,None)))) == Link(4,Link(2,None))
assert lst_sem_rep(Link(2,Link(4,Link(2,None)))) == Link(4,Link(2,None))
assert lst_sem_rep(Link(3,Link(3,Link(3,Link(2,Link(4,Link(2,None))))))) == Link(3,Link(4,Link(2,None)))