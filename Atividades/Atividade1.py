import sys
import re
import collections

cnt = Counter()

def mais_frequentes(palavras, k):
    """
    Encontra as k palavras mais frequentes.
    """
    for palavra in palavras:
        cnt[palavra] += 1
    yield from cnt
	# processar cada palavra
    # achar as palavras mais fequentes
    # imprimir a resposta

def le_palavras(nome_arquivo):
    palavra = re.compile('[a-z]+')
    for linha in open(nome_arquivo):
        yield from palavra.findall(linha.lower())

def main():
    if len(sys.argv) != 3:
        print("Número de argumentos inválido.")
        print("Modo de usar: python3 {} k nome_arquivo", sys.argv[0])
        sys.exit(1)
    k = int(sys.argv[1])
    nome_arquivo = sys.argv[2]
    palavras = le_palavras(nome_arquivo)
    #palavras = list(le_palavras(nome_arquivo))
    mais_frequentes(palavras, k)

    words = re.findall('\w+', open('texts.txt').read().lower())
    Counter(words).most_common(10)
    

if __name__ == "__main__":
    main()