import random

def lancar_dados():
    dado1 = random.randint(1, 6)  
    dado2 = random.randint(1, 6)  
    return dado1, dado2

def calcular_soma(dado1, dado2):
    return dado1 + dado2

# Simulando o lançamento dos dados
dado1, dado2 = lancar_dados()
soma = calcular_soma(dado1, dado2)

print("Resultado do lançamento do dado 1:", dado1)
print("Resultado do lançamento do dado 2:", dado2)
print("Soma dos valores obtidos:", soma)
