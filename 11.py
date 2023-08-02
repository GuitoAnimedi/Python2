import random

def jogo_de_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    while True:
        try:
            palpite = int(input("Digite um número entre 1 e 100: "))
            tentativas += 1

            if palpite < 1 or palpite > 100:
                print("O número deve estar entre 1 e 100.")
            elif palpite < numero_secreto:
                print("Tente um número maior.")
            elif palpite > numero_secreto:
                print("Tente um número menor.")
            else:
                print(f"Parabéns! Você acertou o número secreto {numero_secreto} em {tentativas} tentativa(s).")
                break
        except ValueError:
            print("Digite um número válido.")

def main():
    print("Bem-vindo ao jogo de adivinhação!")
    print("O computador escolherá um número aleatório entre 1 e 100.")
    print("Tente adivinhar qual é o número secreto!")
    jogo_de_adivinhacao()

if __name__ == "__main__":
    main()
