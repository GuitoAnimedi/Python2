def eh_palindromo(palavra):
    palavra = palavra.lower()
    palavra_invertida = palavra[::-1]  

    return palavra == palavra_invertida


palavra1 = "radar"
palavra2 = "jogo"
palavra3 = "arara"

print(eh_palindromo(palavra1))  # Saída: True
print(eh_palindromo(palavra2))  # Saída: False
print(eh_palindromo(palavra3))  # Saída: True
