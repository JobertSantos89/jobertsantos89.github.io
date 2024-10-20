# Listas
# Para declarar listas precisamos utilizar os colchetes, e podemos inicializa-la vazia ou já com valores pré-definidos
# minha_lista = []
# A lista ela é uma estrutura INDEXADA
# Indices:       0     1    2      3
minha_lista = ['Davi', 14, False, 75.3]

# Acessando Elementos
print(minha_lista)
print(minha_lista[2]) # False
print(minha_lista[0]) # 'Davi'

# Adicionar um item a lista:
# Adicionar ao final da lista o elemento dentro do "append"
minha_lista.append('Carlos')
# print(minha_lista) # Descomente para ver o resultado

# Adicionar um item em uma posição especifica (no começo por exemplo):
# Adicionando a posição "0" o valor 2000, os outros elementos são empurrados para a direita
minha_lista.insert(0, 2000)
# print(minha_lista) # Descomente para ver o resultado


# Excluir um item da lista
# valor_excluido = minha_lista.pop(0)
# print(minha_lista) # Descomente para ver o resultado

del minha_lista[3]
print(minha_lista) # Descomente para ver o resultado


# Achando o Index de um Valor
indice = minha_lista.index('Davi')
print(indice)
