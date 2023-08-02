def ler_sequencia_numeros():
    sequencia = []
    while True:
        try:
            num = float(input("Digite um número (ou uma letra para encerrar): "))
            sequencia.append(num)
        except ValueError:
            break
    return sequencia

def encontrar_maior_menor(sequencia):
    if not sequencia:
        return None, None
    maior = menor = sequencia[0]
    for num in sequencia:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    return maior, menor

def main():
    print("Digite uma sequência de números para encontrar o maior e o menor.")
    sequencia = ler_sequencia_numeros()
    maior, menor = encontrar_maior_menor(sequencia)
    if maior is not None and menor is not None:
        print(f"O maior número é: {maior}")
        print(f"O menor número é: {menor}")
    else:
        print("Nenhum número válido foi fornecido.")

if __name__ == "__main__":
    main()
