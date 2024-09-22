# Ex04. Faça um programa que peça para o usuário valores para realizar uma contagem:

# - inicio
# - final
# - passo

# Ao final, mostre uma contagem na tela com os valores fornecidos para o usuário.

inicio = int(input('Digite o inicio da contagem: '))
final = int(input('Digite o final da contagem: '))
passo = int(input('Digite o passo da contagem: '))

for numero in range(inicio, final + 1, passo):
    print(numero, end=' ')