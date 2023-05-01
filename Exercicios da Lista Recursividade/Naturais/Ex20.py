# 20. Projete um algoritmo que receba como entrada um número qualquer a e um número natural n e calcule
# o valor a^n (use recursividade!).
from dataclasses import dataclass
from typing import Union

#Considerando os numero naturais sendo do intervalo
# 0 até n um numero com no maximo 2147483647 caracteres

# Recebe uma um numero qualquer a e um n natural
# e devolve valor a^n.
def sqrt_natural(a: float,n: int ) -> float:
    if 0 == a:
        return 0
    elif a == 1 or n == 0:
        return 1
    else:
        return a * sqrt_natural(a, n-1)

assert sqrt_natural(0, 99) == 0
assert sqrt_natural(1, 66) == 1
assert sqrt_natural(34, 0) == 1
assert sqrt_natural(2, 2) == 4
assert sqrt_natural(3, 4) == 81