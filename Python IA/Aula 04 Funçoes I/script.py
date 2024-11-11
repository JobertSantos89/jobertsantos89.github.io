# Professor: Davi Lucciola
# Sejam bem vindos a aula 04 do modulo de Python.

# Repositório do Github:
# https://github.com/Davi-Classes/PYTHON2024-DFS114
# =============================================================
# Ex01. Faça uma função que receba 2 numeros e retorne o produto entre eles.

def multiplicar(n1: float, n2: float):
    return n1 * n2

num1 = float(input('Digite um numero: '))
num2 = float(input('Digite outro numero: '))

produto = multiplicar(num1, num2)

print(f'Resultado: {produto}')

# ----------------------------------------------------------------------------------------------------------

# Ex02. Faça uma função que receba dois parametros, nome e sobrenome, e retorne o nome completo separado por um espaço.

'Pedro'
'Pereira'
'Pedro Pereira'


def nome_completo(nome: str, sobrenome: str):
    return f'{nome} {sobrenome}'

nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome (Opcional): ')

completo = nome_completo(nome, sobrenome)

print(f'Nome: {completo}.')

# ----------------------------------------------------------------------------------------------------------

# Ex03. Faça uma função que receba uma string qualquer e retorne a quantidade de vogais presentes naquela string.

# ----------------------------------------------------------------------------------------------------------

# Ex04. Faça uma função "fatorial" que receba um numero e retorne o fatorial daquele numero.

# =============================================================
# funcoes1.py


# Funções
# Uma função é uma ação que está sendo executada
# Nós vinhamos utilizando funções o tempo todo, como por exemplo:

# Print
print('Um texto')
print('Outro texto')

# Input
var = input('Digite algo: ')


# ----------------------------------------------------------------------------------------------------------
# funcoes2.py


# Funções 2
# Para definir uma função precisamos utilizar a palavra reservada "def"

# A função é composta por:
# - Parametros (Entrada)
# - Corpo da Função (Processamento)
# - Retorno (Saída)

# Exemplo:

# Type Hint -> Dica de Tipo
# OBS: O type hint não é obrigatório. 
def saudacao(nome: str) -> str:
    return f'Olá {nome}, Seja bem vindo!'

def boas_vindas(mensagem: str) -> None:
    print(f'BOAS VINDAS: {mensagem}')

# Utilizando a função
nome = input('Digite seu nome: ')

# Chamando a função Saudação, passando nome como parametro.
mensagem_saudacao = saudacao(nome)

# Aqui teremos 2 Prints, um da função "boas vindas", 
# o outro é o retorno da função boas vindas (None, poque não foi especificado retorno) 
print(boas_vindas(mensagem_saudacao)) 


# ----------------------------------------------------------------------------------
# funcoes3.py

def somar(n1: int, n2: int):
    return n1 + n2


num1 = int(input('Digite o 1º numero: '))
num2 = int(input('Digite o 2º numero: '))

soma = somar(num1, num2)

print(soma)


# -----------------------------------------------------------------------------------
# funcoes4.py

# Funções 4
# Parametros Opcionais são parametros onde definimos um valor padrão, caso o parametro seja passado na função, ele irá considerar o passado, caso não, ele irá considerar o padrão.

def nome_completo(nome: str, ultimo_nome: str, nome_do_meio: str = ''):
    completo = nome

    if nome_do_meio != '':
        completo += f' {nome_do_meio}'

    completo += f' {ultimo_nome}'
    return completo

nome = input('Digite seu nome: ')
meio = input('Digite seu nome do meio: ')
sobrenome = input('Digite seu sobrenome: ')

# Chamando 3 Parametros
completo = nome_completo(nome, sobrenome, meio)

# Chamando sem o ultimo parametro (que contém valor padrão.)
nome_curto = nome_completo(nome, sobrenome)

print(f'Nome Completo: {completo}.')
print(f'Nome Completo: {nome_curto}.')