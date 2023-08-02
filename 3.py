def imprimir_numeros_ate_n(n):
    if n < 0:
        print("O número deve ser inteiro positivo.")
        return

    for i in range(n + 1):
        print(i)

try:
    numero = int(input("Digite um número inteiro positivo: "))
    imprimir_numeros_ate_n(numero)
except ValueError:
    print("Entrada inválida. Certifique-se de digitar um número inteiro positivo.")
