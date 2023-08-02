def media_lista(numeros):
    if not numeros: 
        return 0

    total = sum(numeros)
    quantidade = len(numeros)
    media = total / quantidade
    return media


lista_de_numeros = [10, 20, 30, 40, 50]
resultado_media = media_lista(lista_de_numeros)
print("A média dos números é:", resultado_media)
