# Entrada: Uma sequência de 𝑛 elementos 𝐴 = ⟨𝑎1,𝑎2,…,𝑎𝑛⟩.
# Saída: A modificação da 𝐴 tal que 𝐴 = ⟨𝑎2,…,𝑎𝑛,𝑎1⟩
sequencia = [5,4,3,2,1]

def ex_2a(lst: list):
    l = len(lst) - 1
    v = lst[0]
    def ex2a(lst2: list, l, n=0):
        if l <= 1:
            return lst2
        elif l == n:
            lst2[l] = v
        if l > n:
            lst2[n] = lst2[n+1]
            ex2a(lst2, l, n+1)

    ex2a(lst, l)

ex_2a(sequencia)
