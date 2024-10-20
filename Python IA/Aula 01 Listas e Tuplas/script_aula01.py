# Sejam Bem Vindos a 1ª Aula do Módulo de Python

# ================================================
# Exercicios

# Ex01. Crie uma lista preenchida com 5 valores:

# -> Mostre na tela o elemento na posição 2
# -> Mostre na tela o 2º elemento da lista

# lista = ['Davi', 'Fernanda', 'Loki', 'Café', 'Margot']

# print(lista[2]) # Posição 2 = 3º Elemento
# print(lista[1]) # Posição 1 = 2º Elemento

# ----------------------------------------------------------------------------------

# Ex02. Faça um programa que começe criando uma lista vazia, e adicione 3 nomes com o "append" utilizando o FOR

# nomes = []

# for n in range(3):
#     nome = input(f'Digite o {n + 1}º nome: ')
#     nomes.append(nome)

# print(nomes)

# ----------------------------------------------------------------------------------

# Ex03. Faça um programa que peça 5 numeros e adicione-os em uma lista, ao final mostre:

# -> Media dos numeros
# -> Maior Numero
# -> Menor Numero

# numeros = []

# # 0 - 4
# for i in range(5):
#     Q
# F    numeros.append(numero)

# maior = max(numeros)
# menor = min(numeros)
# media = sum(numeros) / len(numeros)

# print(f'Maior: {maior}')
# print(f'Menor: {menor}')
# print(f'Média: {media:.2f}')

# ----------------------------------------------------------------------------------

# Ex04. Faça um programa que peça 6 numeros, e armazene-os em 2 listas: pares e impares
# Ao final mostre os valores de ambas as listas

# ----------------------------------------------------------------------------------

# Ex05. Faça um programa que peça nome e categoria de N produtos (o usuário irá determinar quando ele irá parar de cadastrar), ao finalizar os cadastros, mostre o nome e categorias registradas para todos os produtos.

# ================================================
# listas1.py


# # Listas
# # Para declarar listas precisamos utilizar os colchetes, e podemos inicializa-la vazia ou já com valores pré-definidos
# # minha_lista = []
# # A lista ela é uma estrutura INDEXADA
# # Indices:       0     1    2      3
# minha_lista = ['Davi', 14, False, 75.3]

# # Acessando Elementos
# print(minha_lista)
# print(minha_lista[2]) # False
# print(minha_lista[0]) # 'Davi'

# # Adicionar um item a lista:
# # Adicionar ao final da lista o elemento dentro do "append"
# minha_lista.append('Carlos')
# # print(minha_lista) # Descomente para ver o resultado

# # Adicionar um item em uma posição especifica (no começo por exemplo):
# # Adicionando a posição "0" o valor 2000, os outros elementos são empurrados para a direita
# minha_lista.insert(0, 2000)
# # print(minha_lista) # Descomente para ver o resultado


# # Excluir um item da lista
# # valor_excluido = minha_lista.pop(0)
# # print(minha_lista) # Descomente para ver o resultado

# del minha_lista[3]
# print(minha_lista) # Descomente para ver o resultado


# # Achando o Index de um Valor
# indice = minha_lista.index('Davi')
# print(indice)


# ================================================
# listas2.py


# # Listas
# lista = ['Lucas', 'Ricardo', 'Pedro']

# # Iterando a Lista (Diretamente)
# # Quando utilizamos o "FOR" com uma lista, assim como em uma string, ele irá pegar cada elemento da lista, e para cada elemento irá executar o seu bloco de código
# print('---- Nomes Inseridos ----')
# for nome in lista:
#     print(f'- {nome}')


# # Iterando a Lista (Indiretamente)
# # Também podemos iterar as listas utilizando os seus indíces
# # No exemplo abaixo estou utilizando a função "LEN" para buscar o final do range (Como o final é -1, não preciso me preocupar porque o range sempre terá os mesmos indices da lista)
# # Então, dentro do for, acessamos o elemento na posição do indice, em ordem.
# for i in range(len(lista)):
#     print(f'- {lista[i]}')

# UÇ.; NJMO90Y76TSDWE 4DVR  