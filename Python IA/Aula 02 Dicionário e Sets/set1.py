# Set - Conjuntos
# Um conjunto é uma estrutura não ordenada que não pode conter valores repetidos. Seu objetivo é basicamente definir um escopo de valores possiveis.
meu_conjunto = {'maçã', 'banana', 'kiwi', 'kiwi'}
# print(meu_conjunto)

# Removendo valores duplicados
categorias = ['Eletrônico', 'Eletrônico', 'Cozinha', 'Limpeza']
categorias = list(set(categorias))
print(categorias)
