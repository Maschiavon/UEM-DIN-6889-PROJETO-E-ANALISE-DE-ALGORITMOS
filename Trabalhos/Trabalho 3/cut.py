# Implementação dos algoritmos para resolver o problema de corte de hastes
# Veja a seção 5.1 do livro do Cormen
#
# Chame o programa sem argumentos para executar alguns testes.
#
# Para medir o tempo de execução de uma das implementações execute
# python3 cut.py fun n
# onde fun é o nome da função (cut, cut_memo ou cut_it) e n é o tamanho da entrada

from typing import List
import sys

sys.setrecursionlimit(10000)

def cut(n: int, p: List[int]) -> int:
    if n == 0:
        q = 0
    else:
        q = -1
        for i in range(1, n + 1):
            q = max(q, p[i - 1] + cut(n - i, p))
    return q

assert cut(4, [1, 5, 8, 9]) == 10


def cut_memo(n: int, p: List[int], r: List[int] = None) -> int:
    if r == None:
        r = [-1] * (n + 1)
    if r[n] != -1:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = max(p[i - 1] + cut_memo(n - i, p, r) for i in range(1, n + 1))
    r[n] = q
    return r[n]

assert cut_memo(4, [1, 5, 8, 9]) == 10


def cut_it(n: int, p: List[int]) -> int:
    r = [-1] * (n + 1)
    r[0] = 0
    for j in range(1, n + 1):
        r[j] = max(p[i - 1] + r[j - i] for i in range(1, j + 1))
    return r[n]

assert cut_it(4, [1, 5, 8, 9]) == 10


# Verifica por amostragem que cut_memo e cur_it
# produzem o mesmo resultado de cut
def check():
    for n in range(10, 20):
        p = gen(n)
        melhor = cut(n, p)
        assert cut_memo(n, p) == melhor
        assert cut_it(n, p) == melhor


def gen(n: int) -> List[int]:
    import random
    p = list(range(1, 3 * n))
    random.shuffle(p)
    p.sort()
    return p[:n]

def main():
    import sys
    import time
    if len(sys.argv) == 1:
        print('Testando...')
        check()
        print('Ok')
    elif len(sys.argv) == 3:
        f = sys.argv[1]
        n = int(sys.argv[2])
        if f not in ['cut', 'cut_memo', 'cut_it']:
            print(f'Nome da função inválido: {f}')
            print('Os valores válidos são: cut, cut_memo e cut_it')
        else:
            fun = globals()[f]
            print(f'Executando {f} para uma instância aleatória de tamanho n = {n}')
            s = time.time()
            fun(n, gen(n))
            print(f'Tempo {time.time() - s}')
    else:
        print('Número de argumentos inválido')
        print('Modo de uso:')
        print(f'python3 {sys.argv[0]} [cut|cut_meno|cut_it n], onde o primeiro argumento é a função e n é o tamanho do problema')

if __name__ == '__main__':
    main()
