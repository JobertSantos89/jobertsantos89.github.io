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