Sejam Bem Vindos a 2ª Aula de Python:


Repositório da Turma
https://github.com/Davi-Classes/PYTHON2024-DFS114/tree/main

==========================================
Exercicios.


Ex01. Faça um programa onde o usuário deve inserir 5 frutas, ao finalizar a inserção, mostre todas as frutas unicas que foram inseridas. (Remova os Duplicados)


	
==========================================
set1.py


# Set - Conjuntos
# Um conjunto é uma estrutura não ordenada que não pode conter valores repetidos. Seu objetivo é basicamente definir um escopo de valores possiveis.
meu_conjunto = {'maçã', 'banana', 'kiwi', 'kiwi'}
# print(meu_conjunto)

# Removendo valores duplicados
categorias = ['Eletrônico', 'Eletrônico', 'Cozinha', 'Limpeza']
categorias = list(set(categorias))
print(categorias)


----------------------------------------------------------------------------------------------------------------
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