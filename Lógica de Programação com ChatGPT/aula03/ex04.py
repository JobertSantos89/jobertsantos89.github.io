maior_numero = None # Variavel Acumuladora

while True:
    numero = int(input('Digite um numero: '))

    if maior_numero == None or numero > maior_numero:
        maior_numero = numero

    resposta = input('Deseja continuar? [S/N] -> ')

    if resposta == 'N':
        break

print(f'O maior numero digitado foi: {maior_numero}')
print('Fim do Programa!')