# Ex02. Faça um programa que mostre somente os numeros pares entre 0 e 50 (Ambos inclusos)

# Solução 1
for numero in range(0, 51, 2):
    print(numero, end=' ')

print()

# Solução 2
for numero in range(0, 51):
    if numero % 2 == 0:
        print(numero, end=' ')