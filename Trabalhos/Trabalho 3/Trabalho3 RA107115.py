#!/usr/bin/env python3
#
# Implementação de um algoritmo de programação dinâmica para resolver o
# problema do escalonamento de intervalos com peso.
#
# O programa pode ou não receber um nome de arquivo na linha de comando.
# - Se o nome do arquivo não for fornecido, o programa executa um teste.
# - Se o nome do arquivo for fornecido, o programa lê os intervalos
#   do arquivo e faz o escalonamento. Veja a função le_intervalos para
#   um descrição do formato do arquivo.
import sys
from typing import List
from dataclasses import dataclass
# Matheus Augusto Schiavon
# RA: 107115

# Representa um intervalo.
# Requer que s <= f e v > 0.
@dataclass
class Inter:
    s: int  # início
    f: int  # término
    v: int  # peso

# Soma os pesos dos elementos da List[Inter] A
def PesoTotal(A: List[Inter]) -> int:
    soma = 0
    for i in range(len(A)):
        soma += A[i].v
    print('A soma dos pessos do intervalo é:')
    print(soma)
    return soma

# Recebe A uma List[Inter] e retorna A em forma não descrescente de termino.
def Ordenar_termino_naodesc(A: List[Inter], i=0) -> List[Inter]:
    if len(A) <= 1 or i == len(A):
        return A
    else:
        pos = i+1
        while pos <= len(A)-1:
            if A[pos].f <= A[i].f:
                A[i], A[pos] = A[pos], A[i]
            pos += 1
        return Ordenar_termino_naodesc(A, i + 1)

# Recebe A uma lista ordenado em forma não descrescente de
# termino e um indice dessa lista e define p um inteiro que
# representa a quantidade de soluções que não sobrepoem o A[ind].
def DefinirP(A: List[Inter], ind: int, i=1, p=0):
    if ind-i < 0:
        return p
    else:
        s = ind-i
        if A[s].f <= A[ind].s:
            return DefinirP(A, ind, i+1, p+1)
        else:
            return DefinirP(A, ind, i+1, p)

# Recebe uma lista ordenado em forma não descrescente de
# termino e retorna p uma lista de valores de p[0] = 0
# até p[n] onde p na posição n é um valor que representa todas as
# soluções que não sobrepoem o elemento h[n].
def CalcularP(h: List[Inter], n: int):
    p = [-1] * (n + 1)
    p[0] = 0
    for i in range(0, n):
        p[i+1] = DefinirP(h, i)
    return p

# Recebe h uma List[Inter] ordenado em forma não descrescente de
# termino e n o tamanho do problema e devolve r uma lista de soma maxima
# dos intervalos de 0 a n, s uma lista que informa se o elemento na posição n
# pertence a solução daquele problema, faz isso para 0 a n, ou seja, se s[1] = True
# significa que para n=1 o h[n] pertence a solução, e por ultimo p uma lista que vai de
# 0 a n com a quantidade de soluções que não sobrepoem os problemas de 0 a n respectivamente
# por exemplo se p[5] = 3, significa que existem 3 problemas que não sobrepoem h[5].
def Extended_Bottom_Up_Cut_Rod_Com_Peso(h: List[Inter], n: int):
    r = [-1] * (n+1)
    s = [False] * (n+1)
    r[0] = 0
    s[0] = True

    p = CalcularP(h, n)

    for j in range(1, n+1):

        if r[j-1] > h[j-1].v + r[p[j]]:
            r[j] = r[j-1]
            s[j] = False
        else:
            r[j] = h[j-1].v + r[p[j]]
            s[j] = True

    return r, s, p

# Encontra um subconjunto disjunto do intervalos no subarranjo A[0 : n] cuja a
# soma dos pesos seja máxima. A resposta é dada em ordem de início dos
# intervalos.
def escalona_intervalos(A: List[Inter], n: int) -> List[Inter]:
    # ESCREVA A FUNÇÃO PRINCIPAL AQUI.
    # Você vai precisar criar funções auxiliares.
    # Lembre-se que o arranjo é indexado de 0 e o último elemento é n-1.

    if n == 0:
        return []
    else:
        #return Print_Cut_Rod_Solution(A, n)
        (r, s, p) = Extended_Bottom_Up_Cut_Rod_Com_Peso(A, n)
        print('Printando os intervalos:')

        # O loop a seguir inseri os intervalos da solução
        # para A em resultado.
        resultado = []
        l = n
        while l > 0:
            if s[l]:
                resultado.append(A[l - 1])
                l = p[l]
            else:
                l -= 1

        resultado = Ordenar_termino_naodesc(resultado)
        return resultado


# Verifica se a função escalona_intervalos funciona corretamente
# para o exemplo dos slides
def check():
    A = [Inter(1, 6, 8), Inter(0, 2, 4), Inter(4, 8, 6), Inter(7, 9, 2), Inter(3, 5, 3)]
    R = escalona_intervalos(A, 5)
    assert R == [Inter(0, 2, 4), Inter(4, 8, 6)]


# Lê os intervalos a partir do arquivo arq.
# O arquivo deve ter um intervalo por linha no formato
# s f v
def le_intervalos(arq: str) -> List[Inter]:
    inter = []
    for linha in open(arq):
        s, f, v = map(int, linha.split())
        inter.append(Inter(s, f, v))
    return inter


# Mostra o conjunto de intervalos e a soma dos seus pesos
def exibe_solucao(A: List[Inter]):
    soma = sum(i.v for i in A)
    print(A)
    print(f'Soma dos pesos: {soma}')
    print('Intervalos:')
    for i in A:
        print(f'{i.s} {i.f} {i.v}')

def main():
    import sys
    if len(sys.argv) == 1:
        print('Executando o teste com o exemplo do slide')
        check()
        print('Ok')
    if len(sys.argv) == 2:

        A = le_intervalos(sys.argv[1])
        print('Antes modificacao:')
        print(A)
        B = Ordenar_termino_naodesc(A)
        print('Pos modificacao:')
        print(B)

        r = escalona_intervalos(B, len(B))
        exibe_solucao(r)
    else:
        print('Número de parâmetros inválido')
        print('Modo de usar')
        print(f'{sys.argv[0]} [nome-do-arquivo]')

if __name__ == "__main__":
    main()
