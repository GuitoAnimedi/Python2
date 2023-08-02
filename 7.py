def calcular_fatorial(numero):
    if numero < 0:
        return "O fatorial não está definido para números negativos."
    elif numero == 0 or numero == 1:
        return 1
    else:
        fatorial = 1
        for i in range(2, numero + 1):
            fatorial *= i
        return fatorial

numero = int(input("Digite um número inteiro: "))
resultado_fatorial = calcular_fatorial(numero)
print(f"O fatorial de {numero} é: {resultado_fatorial}")
