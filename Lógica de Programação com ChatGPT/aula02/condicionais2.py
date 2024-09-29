# Operadores Lógicos
# - and 
# - or
# - not
# O numero está entre 1 e 10 (incluso)

numero_escolhido1 = 2
numero_escolhido2 = 20

print('Acerte o intervalo e um dos numeros especiais')
numero = int(input('Digite um numero: '))

# And -> as duas condições precisam ser verdadeiras
if numero >= 1 and numero <= 10:
    print('O numero está no intervalo de 1 a 10')
else:
    print('O numero não está no intervalo de 1 a 10')

# Or -> se uma condição for verdadeira
if numero == numero_escolhido1 or numero == numero_escolhido2:
    print('Você acertou um dos numeros escolhidos!')
else:
    print('Você não acertou um dos numeros escolhidos!')