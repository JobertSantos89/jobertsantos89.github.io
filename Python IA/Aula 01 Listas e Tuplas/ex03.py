numeros = []

# 0 - 4
for i in range(5):
    numero = float(input(f'Digite o {i+1}º numero: '))
    numeros.append(numero)

maior = max(numeros)
menor = min(numeros)
media = sum(numeros) / len(numeros)

print(f'Maior: {maior}')
print(f'Menor: {menor}')
print(f'Média: {media:.2f}')