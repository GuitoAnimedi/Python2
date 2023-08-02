def palavras_em_maiusculas(lista_strings):
    palavras_maiusculas = [palavra.upper() for palavra in lista_strings]
    return palavras_maiusculas

lista_strings = ["python", "é", "uma", "linguagem", "de", "programação"]
resultado = palavras_em_maiusculas(lista_strings)
print(resultado)
