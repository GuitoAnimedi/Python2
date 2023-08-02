def ordenar_crescente(lista):
    return sorted(lista)

# Exemplo de uso da função:
numeros = [5, 9, 1, 7, 3]
lista_ordenada = ordenar_crescente(numeros)
print(lista_ordenada)

def ordenar_crescente(lista):
    lista.sort()
    return lista

# Exemplo de uso da função:
numeros = [5, 9, 1, 7, 3]
ordenar_crescente(numeros)
print(numeros)  # A lista original foi modificada e estará ordenada de forma crescente.
