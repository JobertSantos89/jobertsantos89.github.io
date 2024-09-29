# Operadores Relacionais
# >  - Menor que
# <  - Maior que
# <= - Menor ou igual a
# >= - Maior ou igual a
# == - Igual a
# != - Diferente de
# Peça para o usuário dois numeros, e mostre o maior na tela.

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))


if n1 > n2:
    print(f'O numero 1 foi o maior ({n1})')
elif n1 == n2:
    print('Os numeros são iguais.')
else:
    print(f'O numero 2 foi o maior  {n2}')
