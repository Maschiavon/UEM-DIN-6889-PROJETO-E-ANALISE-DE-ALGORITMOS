#Projete um algoritmo alternativo de particionamento (diferente do algoritmo do exercício 1 da prova e
# do algoritmo Partition do livro) e use invariante de laço para mostrar que ele funciona corretamente. *

# Caso Base
# se ele só possuir 1 elemento ele ira devolver esse elemento

# Antes
# considenrando "a" a variavel de um arranjo finito
# pivo um elemento do arranjo que será utilizado na comparação
# r o index de começo dos elementos menores que o pivo
# e j o index do ultimo elemento dos menores
# a[j+1..fim] vai ser o arranjo dos elementos maiores
# e a[r....j] vai ser o arranjo dos elementos menores.

# Manutenção
# essa é uma abordagem top-down
# Apartir da comparação do pivo com o elemento a[i]
# será determinado o que ele ira fazer se for maior
# ele reduz j criando o espaço para os elementos maiores
# se não igualá r = j e cria o espaço para os menores
# e o aumenta conforma acha os menores
# e se ele achar um maior após o array dos menores
# ele troca o lugar desse maior com o lugar do ultimo
# menor e diminui j e r para manter o array em ordem

# Termino
# após o termino o tamanho a posição de j vai estar atualizada
# e o mesmo realizará a manutenção até i = 0 e r = 0
# pois r é o começo dos menores

# O algoritmo de partição2 recebe um arranjo e vai
# organiza-lo da seguinte forma: restante / menores / maiores
# e vai devolver o indice do começo dos maiores
def particao_2(a, ini=0):
    fim = len(a)
    j = fim - 1
    r = 0
    pivo = a[j]
    x = 1
    for i in reversed(range(ini, fim)):
        if a[i] >= pivo:
            if r != fim-1:
                a[i], a[j] = a[j], a[i]
                j -= 1
                r -= 1
            else:
                j -= 1
        elif r != fim and x == 1:
            r = j
            x = 0
        else:
            r -= 1
    return j + 1

a = [8, 5, 12, 55, 3, 7, 82, 44, 35, 25, 41, 29, 17]
b = [8, 18, 12, 55, 3, 7, 82, 44, 35, 9, 41, 29, 17]

print("A antes da partição", a)
print("index do começo dos maiores", particao_2(a))
print("A após a partição", a)

print("B antes da partição", b)
print("index do começo dos maiores", particao_2(b))
print("B após a partição", b)