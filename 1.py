def soma_1_a_100():
    soma = 0
    for num in range(1, 101):
        soma += num
    return soma

resultado = soma_1_a_100()
print("A soma dos números de 1 a 100 é:", resultado)
