# Pergunte ao usuario uma quantidade indeterminada de valores, e toda vez pergunte se ele deseja continuar, e ao final mostre na tela qual foi o maior numero digitado.

maior = None # Variavel acumuladora
resposta = '' # Variavel de Controle

while resposta != 'N':
    print(f'Maior numero atualmente: {maior}')
    numero = int(input('Digite um valor: '))

    if maior == None or numero > maior:
        maior = numero

    resposta = input('Deseja continuar? [S/N] ')


print(f'O maior numero digitado foi {maior}')
print('Fim do Programa!')