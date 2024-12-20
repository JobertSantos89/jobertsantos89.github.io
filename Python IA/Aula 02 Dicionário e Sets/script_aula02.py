# Sejam Bem Vindos a 2ª Aula de Python:


# Repositório da Turma
# https://github.com/Davi-Classes/PYTHON2024-DFS114/tree/main

# ==========================================
# Exercicios.


# Ex01. Faça um programa onde o usuário deve inserir 5 frutas, ao finalizar a inserção, mostre todas as frutas unicas que foram inseridas. (Remova os Duplicados)

frutas = []

for _ in range(5):
    fruta = input('Digite uma fruta: ')
    frutas.append(fruta.capitalize())

frutas = list(set(frutas))

print('Frutas Inseridas: ')
for fruta in frutas:
    print(f'- {fruta}')

# ------------------------------------------------------------------------------------------------

# Ex02. Faça um programa que peça o nome, raça e cor de um animal e armazene as informações em um dicionário. Ao final mostre os valores nas chaves do dicionário.

# ------------------------------------------------------------------------------------------------

# Ex03. Faça um programa que peça o nome, 3 notas de um aluno, e armazene-os em um dicionário, também armazene nesse dicionário a média e a situação do aluno (>= 6 está aprovado, se não reprovado.)

# ------------------------------------------------------------------------------------------------

# Ex04. Faça um programa para realizar uma votação que será armazenada em um dicionário, onde os candidatos são as chaves, e o valor é a quantidade de votos. O programa iniciará com os candidatos preenchidos e deverá perguntar quantos votos serão realizados. Ao final mostre o resultado da votação.

# ------------------------------------------------------------------------------------------------

# Ex05. Faça um programa para cadastrar 3 cursos que serão armazenados em um dicionário onde o nome do curso será a chave, e o valor será outro dicionário contendo "nivel" e "duração"
# Exemplo:

cursos = {
    'Python': {
        'nivel': 2,
        'duracao': 5
    },
    'Javascript': {
        'nivel': 3,
        'duracao': 7
    },
    'Java': {
        'nivel': 5,
        'duracao': 10
    }
}  



	
# ==========================================
dict1.py


# Dicionários
# O dicionario é uma estrutura feita para representar coisas através de ITEMS, que é um conjunto, de uma chave e um valor
pet1 = {
    # Chave : Valor
    'nome': 'Floki', # Item
    'raca': 'Gato',
    'cor': 'Preto'
} 
print(pet1)

# Acessando Valores
# Diretamente (Com a Chave)
# para acessar os valores, sempre faremos isso através da CHAVE
print(pet1['nome']) # Floki
# print(pet1['algo']) # KeyError - A chave não existe

# Com o GET
print(pet1.get('raca'))
print(pet1.get('algo')) # .get() se a chave existir, ele retorna o valor, se não ele retorna None

# Criando / Atualizando Valores de Chaves
# Se existir a chave, ele atualiza, se não existir ele cria
pet1['castrado'] = False
print(pet1)

pet1['castrado'] = True
print(pet1)

# Inserir Informações
pet1['idade'] = float(input('Qual é a idade do pet? '))
print(pet1)
print(pet1.get('idade'))


# ----------------------------------------------------------------------------------------------------------------

set1.py


# Set - Conjuntos
# Um conjunto é uma estrutura não ordenada que não pode conter valores repetidos. Seu objetivo é basicamente definir um escopo de valores possiveis.
meu_conjunto = {'maçã', 'banana', 'kiwi', 'kiwi'}
# print(meu_conjunto)

# Removendo valores duplicados
categorias = ['Eletrônico', 'Eletrônico', 'Cozinha', 'Limpeza']
categorias = list(set(categorias))
print(categorias)


# ----------------------------------------------------------------------------------------------------------------
# Casting de Iteraveis
# Str -> List
lista = list('Minha String')
print(lista)

# List -> Tuple
tupla = tuple(lista)
print(tupla)

# List -> Str (Juntando com '')
string = ''.join(lista)
print(string)

