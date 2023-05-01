from dataclasses import dataclass
from typing import Union, List


@dataclass
class Link:
    primeiro: int
    resto: 'Lista'

    def __repr__(self):
        return f'Link({self.primeiro}, {self.resto})'


Lista = Union[None, Link]
# Uma Lista é um dos valores:
# - None
# - Link(int, Lista)


#################################
# Ordenação por inserção
#################################


# Cria uma nova Lista com os elementos em ordem não decrescente adicionando v em lst.
# Requer que lst esteja ordenada em ordem não decrescente.
def insere_ordenado(v: int, lst: Lista) -> Lista:
    if lst is None:
        return Link(v, None)
    else:
        if lst.primeiro < v:
            # lst.primeiro é menor que v, então ele deve aparecer antes na lista
            return Link(lst.primeiro, insere_ordenado(v, lst.resto))
        else:
            # v é menor ou igual a lst.primeiro, então v deve aparecer antes na lista
            return Link(v, lst)


assert insere_ordenado(3, None) == Link(3, None)
assert insere_ordenado(2, Link(4, Link(10, None))) == Link(2, Link(4, Link(10, None)))
assert insere_ordenado(7, Link(4, Link(10, None))) == Link(4, Link(7, Link(10, None)))


# Cria uma nova Lista com os mesmos valores de lst mas em ordem não decrescente.
def ordenacao_insercao(lst: Lista) -> Lista:
    if lst is None:
        return None
    else:
        return insere_ordenado(lst.primeiro, ordenacao_insercao(lst.resto))

assert ordenacao_insercao(None) == None
assert ordenacao_insercao(Link(3, None)) == Link(3, None)
assert ordenacao_insercao(Link(5, Link(3, Link(7, None)))) == Link(3, Link(5, Link(7, None)))
assert ordenacao_insercao(Link(4, Link(3, Link(1, None)))) == Link(1, Link(3, Link(4, None)))


#################################
# Ordenação por intercalação
#################################

# Calcula a quantidade de elementos de lst
def tamanho(lst: Lista) -> int:
    if lst is None:
        return 0
    else:
        return 1 + tamanho(lst.resto)

assert tamanho(None) == 0
assert tamanho(Link(4, Link(5, Link(2, None)))) == 3

# Produz uma lista com os n primeiros elementos de lst.
# Requer que 0 <= n <= tamanho(lst)
def mantem(n: int, lst: Lista) -> Lista:
    if n <= 0:
        return None
    else:
        return Link(lst.primeiro, mantem(n - 1, lst.resto))

assert mantem(0, Link(1, Link(2, None))) == None
assert mantem(2, Link(4, Link(6, Link(1, Link(2, None))))) == Link(4, Link(6, None))


# Produz uma lista sem os n primeiros elementos de lst.
# Requer que 0 <= n <= tamanho(lst)
def descarta(n: int, lst: Lista) -> Lista:
    if n <= 0:
        return lst
    else:
        return descarta(n - 1, lst.resto)

assert descarta(0, Link(1, Link(2, None))) == Link(1, Link(2, None))
assert descarta(2, Link(4, Link(6, Link(1, Link(2, None))))) == Link(1, Link(2, None))


# Intercala os elementos de A e B e produz uma nova lista em ordem não decrescente.
# Requer que os elementos de A e B estejam em ordem não decrescente.
def intercala(A: Lista, B: Lista) -> Lista:
    if A is None:
        return B
    elif B is None:
        return A
    elif A.primeiro < B.primeiro:
        return Link(A.primeiro, intercala(A.resto, B))
    else:
        return Link(B.primeiro, intercala(A, B.resto))


# Cria uma nova Lista com os mesmos valores de lst mas em ordem não decrescente.
def ordenacao_intercalacao(lst: Lista) -> Lista:
    if lst is None or lst.resto is None:
        return lst
    else:
        metade = tamanho(lst) // 2
        A = mantem(metade, lst)
        B = descarta(metade, lst)
        C = ordenacao_intercalacao(A)
        D = ordenacao_intercalacao(B)
        return intercala(C, D)


assert ordenacao_intercalacao(None) == None
assert ordenacao_intercalacao(Link(3, None)) == Link(3, None)
assert ordenacao_intercalacao(Link(5, Link(3, Link(7, None)))) == Link(3, Link(5, Link(7, None)))
assert ordenacao_intercalacao(Link(4, Link(3, Link(1, None)))) == Link(1, Link(3, Link(4, None)))



#################################
# Ordenação por troca de partição
#################################


# Produz uma Lista com os elementos de lst menores que v
def menores_ou_iguais(lst: Lista, v: int) -> Lista:
    if lst is None:
        return None
    else:
        if lst.primeiro < v:
            return Link(lst.primeiro, menores_ou_iguais(lst.resto, v))
        else:
            return menores_ou_iguais(lst.resto, v)

assert menores_ou_iguais(None, 5) == None
assert menores_ou_iguais(Link(3, Link(2, Link(7, Link(8, None)))), 4) == Link(3, Link(2, None))


# Produz uma Lista com os elementos de lst maiores que v
def maiores(lst: Lista, v: int) -> int:
    if lst is None:
        return None
    else:
        if lst.primeiro > v:
            return Link(lst.primeiro, maiores(lst.resto, v))
        else:
            return maiores(lst.resto, v)

assert maiores(None, 5) == None
assert maiores(Link(3, Link(2, Link(7, Link(8, None)))), 4) == Link(7, Link(8, None))


# Produz uma Lista com os elementos de lst1 seguidos dos elementos de lst2
def concatena(lst1: Lista, lst2: Lista) -> Lista:
    if lst1 is None:
        return lst2
    else:
        return Link(lst1.primeiro, concatena(lst1.resto, lst2))

assert concatena(None, Link(3, Link(2, None))) == Link(3, Link(2, None))
assert concatena(Link(5, Link(4, None)), Link(3, Link(2, None))) == Link(5, Link(4, Link(3, Link(2, None))))


# Cria uma nova Lista com os mesmos valores de lst mas em ordem não decrescente.
def ordenacao_quicksort(lst: Lista) -> Lista:
    if lst is None:
        return None
    else:
        pivo = lst.primeiro
        A = menores_ou_iguais(lst.resto, pivo)
        B = maiores(lst.resto, pivo)
        C = ordenacao_quicksort(A)
        D = ordenacao_quicksort(B)
        return concatena(C, Link(pivo, D))

assert ordenacao_quicksort(None) == None
assert ordenacao_quicksort(Link(3, None)) == Link(3, None)
assert ordenacao_quicksort(Link(5, Link(3, Link(7, None)))) == Link(3, Link(5, Link(7, None)))
assert ordenacao_quicksort(Link(4, Link(3, Link(1, None)))) == Link(1, Link(3, Link(4, None)))
assert ordenacao_quicksort(Link(4, Link(3, Link(2, Link(1, Link(0, None)))))) == Link(0, Link(1, Link(2, Link(3, Link(4, None)))))


def main():
    from timeit import Timer
    import sys
    import random
    import matplotlib.pyplot as plt

    # Aumenta o número máximo de chamadas recursivas
    sys.setrecursionlimit(10000)

    # Cria uma Lista com os elementos do arranjo A[0 : n].
    # Requer que 0 <= n <= len(A).
    def build(A: List[int], n: int) -> Lista:
        if n == 0:
            return None
        else:
            return Link(A[n - 1], build(A, n - 1))

    TAMANHOS = list(range(100, 1050, 50))
    VEZES = 30

    tempos_insercao = []
    tempos_intercal = []
    tempos_quick = []

    caso = sys.argv[1]
    for n in TAMANHOS:
        print("Tamanho", n)
        lst = list(range(n))
        if caso == "melhor":
            lst.reverse()
        elif caso == "medio":
            random.shuffle(lst)
        else:
            assert caso == "pior"
        lst = build(lst, n)

        tempos_insercao.append(Timer(lambda: ordenacao_insercao(lst)).timeit(VEZES) / VEZES)
        tempos_intercal.append(Timer(lambda: ordenacao_intercalacao(lst)).timeit(VEZES) / VEZES)
        if caso != 'melhor':
            tempos_quick.append(Timer(lambda: ordenacao_quicksort(lst)).timeit(VEZES) / VEZES)

    print(tempos_insercao)
    print(tempos_intercal)
    print(tempos_quick)

    plt.xlabel('Tamanho')
    plt.ylabel('Tempo (s)')
    plt.plot(TAMANHOS, tempos_insercao)
    plt.plot(TAMANHOS, tempos_intercal)
    if caso != 'melhor':
        plt.plot(TAMANHOS, tempos_quick)
        plt.legend(["Inserção", "Intercalação", "Quick"], loc ="upper left")
    else:
        plt.legend(["Inserção", "Intercalação"], loc ="upper left")
    plt.show()

if __name__ == "__main__":
    main()
