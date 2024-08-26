# Sejam bem vindos a primeira aula de lógica de programação


# Lista de Exercicios: https://wiki.python.org.br/EstruturaSequencial
# Playlist para revisar e praticar: https://www.youtube.com/watch?v=S9uPNppGsGo&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0

# ---------------------------------------------------------------
# Exercicios

# Ex 1. Façam um algorimo, considerando que vocês estão no quarto, para preparar um café.

# LEVANTAR
# SAIR do quarto
# IR até a cozinha
# IR até o armario
# PEGAR café
# PEGAR chaleira
# COLOCAR agua na chaleira
# ESQUENTAR chaleira no fogão
# PEGAR coador
# ESPERAR agua da chaleira ferver
# PEGAR garrafa termica
# COLOCAR café no coador
# COAR café com a garrafa termica abaixo
# APROVEITAR café

# ---------------------------------------------------------------------------------------------------------
# Ex 2. Faça um programa que peça o dia, o mês e o ano de nascimento da pessoa utilizando o input, e mostre sua data de nascimento completa.
# Exemplo
# Entrada:
# >>> Ano de Nascimento: 2000
# >>> Mês de Nascimento: 03
# >>> Dia de Nascimento: 10

# Saida
# >>> Sua data de nascimento é 10/03/2000


dia = input('Digite o dia de seu nascimento: ')
mes = input('Digite o mês de seu nascimento: ')
ano = input('Digite o ano de seu nascimento: ')

print(f'Sua data de nascimento é {dia}/{mes}/{ano}')
print('Sua data de nascimento é ' + dia + '/' + mes + '/' + ano)


# -----------------------------------------------------------------------------
# ola_mundo

print('Olá Mundo!')

# -------------------------------------------------------------------------
# variaveis

# Variaveis
# Caixa, onde você pode armazenar uma informação

# Tipos Primitivos
nome = 'Pedro' # string -> str
idade = 23 # inteiro -> int
altura = 1.86 # decimal -> float
tem_filhos = False # booleano -> bool


# -------------------------------------------------------------------------------
# entrada_saida

# Entrada -> Processamento -> Saída
# Input + Variavel = Entrada
nome = input('Digite seu nome: ')

# Saida = Print
# Concatenação
print("Olá " + nome + ", seja bem vindo!")

# F-String
print(f"Olá {nome}, seja bem vindo!")


# -------------------------------------------------------------------------------
# operadores_aritmeticos

# Operadores Aritméticos
# + (Soma)
# - (Subtração)
# * (Multiplicação)
# / (Divisão)


numero1 = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))

soma = numero1 + numero2

print(f'A soma é: {soma}')
