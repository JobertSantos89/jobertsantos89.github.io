# Olá sejam bem vindos a aula 5 do modulo de Python! Funções 2.
# Numero Davi: 31986997442

# Grupo:
# https://chat.whatsapp.com/BaBtIuDJTfdBkOuvsh4a8Q

# Repositório da Turma:
# https://github.com/Davi-Classes/PYTHON2024-DFS114

# ==================================================================
# Ex01. Faça uma função chamada "calcular_media" que recebe 3 notas como parametro e retorna a média aritimética. 
# -> Faça um programa para utilizar a sua função. 

def calcular_media(nota1: float, nota2: float, nota3: float) -> float:
    media = (nota1 + nota2 + nota3) / 3
    return media

n1 = float(input('Digite a 1ª nota: '))
n2 = float(input('Digite a 2ª nota: '))
n3 = float(input('Digite a 3ª nota: '))

media = calcular_media(n1, n2, n3)

print(f'A média do aluno é {media:.2f}')

# -------------------------------------------------------------------------------------------------------

# Ex02. Faça uma função chamada "calcular_imc" que recebe o peso e a altura como parametro e retorna o valor do IMC.
# a) Faça um programa para utilizar a sua função. 
# b) Faça uma função chamada "classificar_imc", que receberá o IMC e irá retornar um dos status: "ABAIXO_DO_PESO", "PESO_IDEAL", "SOBREPESO", "OBESIDADE_I", "OBESIDADE_II", "OBSIDADE_III"

def calcular_imc(peso: float, altura: float) -> float:
    return peso / altura ** 2

def classificar_imc(imc: float) -> str:
    if imc < 18.5:
        return 'ABAIXO_DO_PESO'
    elif imc < 25:
        return 'PESO_IDEAL'
    elif imc < 30:
        return 'SOBREPESO'
    elif imc < 35:
        return 'OBESIDADE_I'
    elif imc < 40:
        return 'OBESIDADE_II'
    else:
        return 'OBSIDADE_III'


peso = float(input('Digite um peso: '))
altura = float(input('Digite uma altura: '))

imc = calcular_imc(peso, altura)
situacao = classificar_imc(imc)

print(f'O seu imc é: {imc:.2f}')
print(f'Situação: {situacao}')

# -------------------------------------------------------------------------------------------------------
# 03. Faça Exuma função chamada "verificar_primo" que recebe um numero inteiro e retorna um booleano (True = Numero é primo, False = Numero não primo)

# -------------------------------------------------------------------------------------------------------

# Ex04. Faça um programa de calculadora implementando os itens abaixo:

# a) Faça uma função chamada "menu" que mostra as opções abaixo na tela, depois pede um valor para o usuário e retorna esse valor somente se ele estiver contido nas opções.

# """
# === Calculadora ===
# [1] - Somar
# [2] - Subtrair
# [3] - Multiplicar
# [4] - Dividir
# ===================
# Digite uma opção: 
# """

# Exemplo 1:
# >>> Digite uma opção: 5 
# Opção Inválida! Digite novamente!
# >>> Digite uma opção: 3
# ...

# b) Faça uma função calculadora, que recebe 3 parametros: num1, num2 e operacao (operacao pode ser 1=Somar, 2=Subtrair, 3=Multiplicar, 4=Dividir) e retorne o resultado do calculo baseado na operação informada.


# ==================================================================
# revisao1.py

# Revisão Funções 1

# def <nome_funcao>(...<parametros>):
#   ... # Corpo da função

def somar(a, b, c):
    resultado = a + b + c
    return resultado


# Chamando a Função
# Exemplo 1
n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
n3 = int(input('Digite o 3º valor: '))

soma = somar(n1, n2, n3)
print(f'Primeira Chamada: {soma}')

# Exemplo 2
valor = somar(3, 6, 7)
print(f'Segunda Chamada: {valor}')

# -------------------------------------------------------------------------------------------------------
# # Revisão Funções 2

# Type Hints
def dividir(num1: float, num2: float) -> float:
    return num1 / num2

# Passagem de Parametros
# Posicional
# 10 -> num1
# 2 -> num2
valor1 = dividir(10, 2)

# Nomeada
# 10 -> num2
# 2 -> num1
valor2 = dividir(num2=10, num1=2)

# Valores Padrão
def subtrair(num1: float, num2: float, num3: float = 0) -> float:
    return num1 - num2 - num3

# Se num3 for passado, ele considera o que foi informado.
resultado1 = subtrair(10, 2, 4) 

# Se num3 não for passado, ele considera o valor padrão.
resultado2 = subtrair(10, 5)