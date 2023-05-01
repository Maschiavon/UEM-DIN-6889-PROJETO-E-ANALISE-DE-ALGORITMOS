# Entrada: Uma sequência de 𝑛 = 2𝑘 +1 elementos ordenados, onde 𝑘 é um número natural, tal que na sequência
# aparecem 𝑘 + 1 elementos distintos, sendo que 𝑘 elementos aparecem duas vezes.
# Saída: O valor do elemento que aparece apenas uma vez. (Por exemplo, para a sequência de entrada
# ⟨4, 4, 7, 7, 8, 9, 9⟩ a resposta é 8.)
# Considerando o indice inicial 0
sequencia = [4, 4, 7, 7, 8, 9, 9]
sequencia2 = [3, 4, 4, 7, 7, 8, 8, 9, 9]

def Achar_unico(lst: list, a=0) -> int:
    if len(lst) == 1:
        return lst[0]
    else:
        if lst[a] == lst[a+1]:
            return Achar_unico(lst, a+2)
        else:
            return lst[a]

print(Achar_unico(sequencia))
print(Achar_unico(sequencia2))