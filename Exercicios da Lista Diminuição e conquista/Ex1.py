# 1. Projete um algoritmo que receba como entrada um número a ̸= 0 e um número natural n e calcule o
# valor "a" elevado a n. Seu algoritmo deve ser O(lg n). Dica: verifique se n é par ou ímpar e 
# diminua o problema de forma apropriada.

# Recebe 2 inteiros "a" e n e devolve
# "a" elevado a n.
def sqrt_recursiva(a: int, n: int) -> int:
    if n == 0:
        return 1
    elif a <= 1:
        return a
    else:
        if (n % 2) == 0:
            return a * a * sqrt_recursiva(a, n - 2)
        else:
            return a * sqrt_recursiva(a, n - 1)


def sqrt_interativo(a: int, n: int) -> int:
    v = a
    while n - 1 != 0:
        if n == 0:
            v = 1
            break
        elif a <= 1:
            v = a
            break
        else:
            v = v * a
            n = n - 1
    return v


e1 = sqrt_recursiva(3, 2)
e2 = sqrt_interativo(3, 2)
e3 = sqrt_recursiva(5, 3)
e4 = sqrt_interativo(5, 3)
e5 = sqrt_recursiva(10, 7)
e6 = sqrt_interativo(10, 7)

assert e1 == 9
assert e2 == 9
assert e3 == 125
assert e4 == 125
assert e5 == 10000000
assert e6 == 10000000
print(e1, e2, e3, e4, e5, e6)
