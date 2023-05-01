# Entrada: Uma sequência de 𝑛 elementos 𝐴 = ⟨𝑎1,𝑎2,…,𝑎𝑛⟩.
# Saída: A modificação da 𝐴 tal que 𝐴 = ⟨𝑎2,…,𝑎𝑛,𝑎1⟩
sequencia = [1,2,3,4,5]

def ex_2b(lst: list):
    i = 0
    v = 0
    l = len(lst)-1
    while i <= l:
        if i == 0:
            v = lst[i]
        elif i == l:
            lst[l] = v
        lst[i] = lst[i + 1]
        i += 1

ex_2b(sequencia)