import string

def contar_ocorrencias_palavras(texto):
    texto_processado = texto.translate(str.maketrans('', '', string.punctuation)).lower()
    palavras = texto_processado.split()

    ocorrencias = {}
    for palavra in palavras:
        ocorrencias[palavra] = ocorrencias.get(palavra, 0) + 1

    return ocorrencias

def main():
    print("Digite o texto:")
    texto = input()

    resultado = contar_ocorrencias_palavras(texto)

    print("Ocorrências de cada palavra no texto:")
    for palavra, ocorrencias in resultado.items():
        print(f"{palavra}: {ocorrencias}")

if __name__ == "__main__":
    main()
