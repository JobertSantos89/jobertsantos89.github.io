import random

def lancar_dados():
    
    dado1 = random.randint(1, 6)

    dado2 = random.randint(1, 6)

    print(f"Dado 1: {dado1}, Dado 2: {dado2}")

    soma = dado1 + dado2

    # Retornar o resultado da soma
    return soma

if __name__ == "__main__":
    resultado = lancar_dados()
    print(f"O resultado do lançamento dos dois dados foi: {resultado}")
