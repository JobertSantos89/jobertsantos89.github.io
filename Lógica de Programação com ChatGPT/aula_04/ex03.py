soma = 0
contador = 1

qtd_numeros = int(input('Quantos numeros deseja somar? '))

while contador <= qtd_numeros:
    numero = float(input('Digite um numero: '))
    
    soma += numero

    contador += 1

print(f'A soma dos valores é: {soma}')