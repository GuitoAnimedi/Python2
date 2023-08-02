def calcular_mediana(lista):
    lista_ordenada = sorted(lista)
    tamanho = len(lista_ordenada)

    if tamanho % 2 == 0:
        meio = tamanho // 2
        mediana = (lista_ordenada[meio - 1] + lista_ordenada[meio]) / 2
    else:
        meio = tamanho // 2
        mediana = lista_ordenada[meio]

    return mediana

numeros = [5, 9, 1, 7, 3]
mediana = calcular_mediana(numeros)
print(f"A mediana dos números é: {mediana}")
