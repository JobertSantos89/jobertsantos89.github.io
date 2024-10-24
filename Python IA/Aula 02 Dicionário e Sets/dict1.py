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