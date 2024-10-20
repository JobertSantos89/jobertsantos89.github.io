# Ex04. Faça um programa que peça 6 numeros, e armazene-os em 2 listas: pares e impares
# Ao final mostre os valores de ambas as listas

pares = []
impares = []

for i in range(1, 7):
    numero = int(input(f'Digite o {i}º numero: '))

    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)


print(f'Pares: {pares}')
print(f'Impares: {impares}')