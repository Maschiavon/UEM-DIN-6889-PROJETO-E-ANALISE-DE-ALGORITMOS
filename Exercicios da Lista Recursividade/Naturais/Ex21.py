# 21. Projete um algoritmo que receba como entrada dois números Natural1, n e x, e devolva uma Lista
# com os divisores de x que são menores ou iguais a n (não se preocupe com a ordem dos valores na
# resposta).
from dataclasses import dataclass
from typing import Union


# Considerando os numero naturais sendo do intervalo
# 0 até n um numero com no maximo 2147483647 caracteres
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
# Exemplos
x: Lista = None
y: Lista = Link(10, None)
z: Lista = Link(20, Link(4, None))


# Insere o elemento "a" no final da lista
def Inserir_Final(lst: Lista, a: int) -> Lista:
    if lst is None:
        return Link(a, None)
    else:
        return Link(lst.primeiro, Inserir_Final(lst.resto, a))


assert Inserir_Final(None, 3) == Link(3, None)
assert Inserir_Final(Link(4, None), 3) == Link(4, Link(3, None))
assert Inserir_Final(Link(3, Link(4, None)), 7) == Link(3, Link(4, Link(7, None)))

# Recebe 2 numeros naturais qualquer x e n
# e devolve uma lista com  os divisores de x
# que são menores ou iguais a n
def divisoresX_n(x: int, n: int) -> Lista:
    if n == 1:
        return Link(1, None)
    else:
        if x % n == 0:
            return Link(n, divisoresX_n(x, n - 1))
        else:
            return divisoresX_n(x, n - 1)

assert divisoresX_n(100, 1) == Link(1, None)
assert divisoresX_n(3, 3) == Link(3, Link(1, None))
assert divisoresX_n(15, 3) == Link(3, Link(1, None))
assert divisoresX_n(8, 8) == Link(8, Link(4, Link(2, Link(1, None))))
assert divisoresX_n(2, 2) == Link(2, Link(1, None))
