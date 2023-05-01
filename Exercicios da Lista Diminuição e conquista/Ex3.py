# 3. Projete um algoritmo que verifique se um arranjo é palíndromo.

# Recebe um arranjo e verifica se
# ele é palíndromo
def ver_palin(lista: list, x=0) -> bool:
    if len(lista) <= 1 or lista is None:
        return True
    else:
        if x == (len(lista) - x) or x == (len(lista) - x - 1):
            return True
        if lista[x] == lista[len(lista) - x - 1]:
            return ver_palin(lista, x+1)
        else:
            return False

lista0 = []
lista1 = [1]
lista2 = [1, 5, 2, 6]
lista3 = [1, 2, 3, 4, 5]
lista4 = [1, 2, 3, 4, 3, 2, 1]
lista5 = [1, 2, 3, 4, 4, 3, 2, 1]

print(ver_palin(lista0))
print(ver_palin(lista1))
print(ver_palin(lista2))
print(ver_palin(lista3))
print(ver_palin(lista4))
print(ver_palin(lista5))
