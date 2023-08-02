def numeros_pares(lista):
    numeros_pares = [numero for numero in lista if numero % 2 == 0]
    return numeros_pares

lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_de_pares = numeros_pares(lista_de_numeros)
print("Números pares:", lista_de_pares)
