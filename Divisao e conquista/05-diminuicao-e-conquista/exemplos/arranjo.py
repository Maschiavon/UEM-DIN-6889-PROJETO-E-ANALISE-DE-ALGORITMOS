from typing import List

# Inverte as posições dos elementos de A.
# O primeiro troca com o último,
# o segundo com o penúltimo,
# e assim por diante.
# Requer que 0 <= n <= len(A).
def inverte(A: List[int], n: int):
    if n <= 1:
        return
    else:
        inverte(A, n - 1)
        move_inicio(A, n - 1)

# Move o A[n - 1] para o inicío A[0].
# Requer que 0 <= n < len(A).
def move_inicio(A: List[int], n: int):
    ultimo = A[n]
    # Invariante:
    # O subarranjo A[i + 1 : n + 1] contém os elementos
    # inicialmente em A[i : n]
    i = n
    while i != 0:
        A[i] = A[i - 1]
        i -= 1
    A[0] = ultimo

ex = []
inverte(ex, 0)
assert ex == []

ex = [4]
inverte(ex, 1)
assert ex == [4]

ex = [1, 3, 4, 5, 2]
inverte(ex, len(ex))
assert ex == [2, 5, 4, 3, 1]


# Inverte as posições dos elementos de A[a : b].
# A[a] troca com A[b-1],
# A[a+1] troca com A[b-2],
# e assim por diante.
# Requer que 0 <= a <= b <= len(A).
def inverte2(A: List[int], a: int, b: int):
    if (b - a) <= 1:
        return
    else:
        inverte2(A, a + 1, b - 1)
        A[a], A[b - 1] = A[b - 1], A[a]

ex = []
inverte2(ex, 0, 0)
assert ex == []

ex = [4]
inverte2(ex, 0, 1)
assert ex == [4]

ex = [1, 3, 4, 5, 2]
inverte2(ex, 0, len(ex))
assert ex == [2, 5, 4, 3, 1]


# Inverte as posições dos elementos de A[a..b].
# A[a] troca com A[b-1],
# A[a+1] troca com A[b-2],
# e assim por diante.
# Requer que 0 <= a <= b <= len(A).
def inverte2_it(A: List[int], a: int, b: int):
    # Invariantes:
    # O subarranjo A[a_inicial : a] contem os
    # valores inicialmente em A[b : b_inicial]
    # mas em ordem invertida.
    # O subarranjo A[b : b_inicial] contem os
    # valores inicialmente em A[a_inicial : a]
    # mas em ordem invertida.
    while (b - a) > 1:
        A[a], A[b - 1] = A[b - 1], A[a]
        a += 1
        b -= 1

ex = []
inverte2_it(ex, 0, 0)
assert ex == []

ex = [4]
inverte2_it(ex, 0, 1)
assert ex == [4]

ex = [1, 3, 4, 5, 2]
inverte2_it(ex, 0, len(ex))
assert ex == [2, 5, 4, 3, 1]


# Produz True se v está em A[a : b];
# False caso contrário.
# Requer que 0 <= a <= b <= len(A).
def busca_binaria(v: int, A: List[int], a: int, b: int) -> bool:
    if a == b:
        return False
    else:
        meio = (a + b) // 2
        if v == A[meio]:
            return True
        elif v < A[meio]:
            return busca_binaria(v, A, a, meio)
        else:
            return busca_binaria(v, A, meio + 1, b)

assert busca_binaria(2, [], 0, 0) == False
assert busca_binaria(2, [2], 0, 1) == True
assert busca_binaria(3, [2], 0, 1) == False
assert busca_binaria(2, [2, 6, 10, 12, 17], 0, 5) == True
assert busca_binaria(6, [2, 6, 10, 12, 17], 0, 5) == True
assert busca_binaria(10, [2, 6, 10, 12, 17], 0, 5) == True
assert busca_binaria(12, [2, 6, 10, 12, 17], 0, 5) == True
assert busca_binaria(17, [2, 6, 10, 12, 17], 0, 5) == True
assert busca_binaria(3, [2, 6, 10, 12, 17], 0, 5) == False
assert busca_binaria(13, [2, 6, 10, 12, 17], 0, 5) == False
assert busca_binaria(23, [2, 6, 10, 12, 17], 0, 5) == False


# Produz True se v está em A[a : b];
# False caso contrário
# Requer que 0 <= a <= b <= len(A).
def busca_binaria_it(v: int, A: List[int], a: int, b: int) -> bool:
    # Invariante:
    # Se v está em A[a_original : b_original]
    # então v está em A[a : b]
    while a < b:
        meio = (a + b) // 2
        if v == A[meio]:
            return True
        elif v < A[meio]:
            b = meio
        else:
            a = meio + 1
    return False

assert busca_binaria_it(2, [], 0, 0) == False
assert busca_binaria_it(2, [2], 0, 1) == True
assert busca_binaria_it(3, [2], 0, 1) == False
assert busca_binaria_it(2, [2, 6, 10, 12, 17], 0, 5) == True
assert busca_binaria_it(6, [2, 6, 10, 12, 17], 0, 5) == True
assert busca_binaria_it(10, [2, 6, 10, 12, 17], 0, 5) == True
assert busca_binaria_it(12, [2, 6, 10, 12, 17], 0, 5) == True
assert busca_binaria_it(17, [2, 6, 10, 12, 17], 0, 5) == True
assert busca_binaria_it(3, [2, 6, 10, 12, 17], 0, 5) == False
assert busca_binaria_it(13, [2, 6, 10, 12, 17], 0, 5) == False
assert busca_binaria_it(23, [2, 6, 10, 12, 17], 0, 5) == False
