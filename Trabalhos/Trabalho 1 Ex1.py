#Projete um algoritmo que verifique se os elementos de um arranjo estão em ordem não decrescente.

# Caso Base
# Se o arranjo só possuir um elemento
# ele estará automaticamente ordenado

# Antes
# considenrando "arranjo" a variavel de um arranjo finito e "a"
# um numero inteiro positivo que começa em 1.
# o arranjo está ordenado até a posição a, arranjo[0...a-1] está ordenado
# e como a começa em 1 de arranjo[0...1-1] = arranjo[0...0] = arranjo[0] está ordenado
# pelo caso base se ele só possuir 1 elemento está ordenado.

# Manutenção
# A manutenção ocorre na comparação de arranjo[a] < arranjo[a - 1]
# se for verdadeiro retorna falso pois o numero em no indice a-1
# não pode ser maior que o numero no indice a, mas ele estiver
# ordenado, ou seja, arranjo[a] < arranjo[a - 1] é falso ele faz a
# chamada recursiva incrementando a em 1 para a comparação dos proximos
# elementos e mantem a invarialvel "o arranjo está ordenado até a posição a" correta.

# Termino
# O algoritmo ira "terminar" se arranjo[a] < arranjo[a - 1] for
# verdadeiro e retornará false ou até quando ele chegar no final do arranjo

# Recebe um arranjo e verifica se
# a ordem está em não descrescente
def arranjo_ordenado(arranjo: list, a=1) -> bool:
    if len(arranjo) <= 1 or len(arranjo) == a:
        return True
    else:
        if arranjo[a] < arranjo[a - 1]:
            return False
        else:
            return arranjo_ordenado(arranjo, a + 1)


#Alguns exemplos a seguir
arranjo1 = [3]
arranjo2 = [3, 5, 4, 6]
arranjo3 = [1, 2, 3, 4, 5]
arranjo4 = [1, 2, 3, 4, 5, 6, 1]

print(arranjo_ordenado(arranjo1))
print(arranjo_ordenado(arranjo2))
print(arranjo_ordenado(arranjo3))
print(arranjo_ordenado(arranjo4))