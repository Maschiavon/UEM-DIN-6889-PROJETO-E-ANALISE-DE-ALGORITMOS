# Projete um algoritmo com tempo de execução O(lg n) que encontre o maior elemento de um arranjo
# não vazio de inteiros com a seguinte característica: os elementos iniciais estão em ordem
# crescente e o restante dos elementos em ordem decrescente. Argumente porque o seu algoritmo
# funciona e faça a análise do tempo de execução (Dicas: faça diversos exemplos para entender
# como o algoritmo deve funcionar. Implemente o algoritmo em uma linguagem de programação e
# teste os exemplos. Faça o algoritmo recursivo, escreva a equação de recorrência para o tempo
# de execução e use o método mestre para resolver a recorrência). *

# Caso Base
# Como a é um arranjo de pelo menos 1 elemento
# se ele só possuir 1 elemento ele ira devolver esse elemento.

# Antes
# Por padrão os elementos iniciais estão em ordem
# crescente e o restante dos elementos em ordem decrescente.
# então a invariante é que dentro do intervalo a[0...len(a)]
# está o maior elemento.

# Manutenção
# Ele recebe um arranjo de tamanho n corta o tamanho pela metade
# e arredonda para baixo, e armazena o resultado na varivel tam
# e compara a[tam-1] <= a[tam] para verficar de qual lado está o maior
# elemento e faz uma chamada recursiva na metade que possui o maior
# mantendo a invariante correta.

# Termino
# após ele ter escolhido uma das metades ele reduziu o problema ao "meio"
# descartando a outra metade de possibilidades invalidas mantendo a invariante.

# Analize do Tempo do Algoritmo
# Como cada comparação elimina cerca de metade dos itens restantes a serem
# considerados a pergunta é qual seria o numero maximo de comparações ?

# Comparações - Número aproximado de itens restantes
#     1       -        n/2
#     2       -        n/4
#     3       -        n/8
#     ...
#     i       -        n/2^i

# e como n/2^i = 1, pois ele irá discartar problemas até o caso base
# se isolarmos i temos:
# n/2^i = 1
# n = 2^i
# log(n) = log(2^i)
# log(n) = i.
# Conclusão o número máximo de comparações é o logaritmo do número de itens na lista.
# Portanto, a get_maior é O(log n).

# Recebe um arranjo a e devolve o maior
# elemento
def get_maior(a):
    if len(a) == 1:
        return a[0]
    else:
        tam = round(len(a)/2)
        if a[tam-1] <= a[tam]:
            arry = a[tam:len(a)]
            return get_maior(arry)
        else:
            arry = a[0:tam]
            return get_maior(arry)

a = [0]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c = [1, 5, 4, 3, 2]
d = [-1, 2, 3, 0]
e = [20, 5, 3, 2, 1]

print("Arranjo completo A", a)
print("Maior:", get_maior(a))

print("Arranjo completo B", b)
print("Maior:", get_maior(b))

print("Arranjo completo C", c)
print("Maior:", get_maior(c))

print("Arranjo completo D", d)
print("Maior:", get_maior(d))

print("Arranjo completo D", e)
print("Maior:", get_maior(e))