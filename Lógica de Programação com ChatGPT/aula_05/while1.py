# Faça um programa que peça uma quantidade indefinida de numeros, após cada numero pergunte se o usuário deseja continuar, quando ele responder não mostre a soma de todos os numeros

soma = 0

while True:
    numero = float(input('Digite um numero: '))
    soma += numero

    while True:
        resposta = input('Deseja continuar? [S/N] ').upper()

        if resposta == 'S' or resposta == 'N':
            break
            
        print('Opção Inválida, digite novamente...')

    if resposta == 'N':
        break

print(f'A soma dos valores é: {soma}')
print('Fim do programa')