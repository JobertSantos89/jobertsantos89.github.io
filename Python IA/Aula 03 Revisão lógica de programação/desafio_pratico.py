# Gerenciamento de Compras de Produtos

# Você foi contratado para desenvolver um programa simples para
# auxiliar em um processo de compra de produtos. O programa deve
# permitir ao usuário inserir o nome e o preço de vários produtos,
# perguntando se deseja continuar inserindo mais produtos após cada
# entrada. Ao final, o programa deve fornecer um resumo da compra,

# incluindo:

# A) O total gasto na compra.

# B) A quantidade de produtos que custam mais de R$1000.

# C) O nome do produto mais barato.
# Desenvolva o programa em Python utilizando conceitos de
# entrada/saída de dados, condicionais e laços de repetição.

# Inicializando variáveis
total_gasto = 0
produtos_acima_1000 = 0
produto_mais_barato = ''
preco_produto_mais_barato = float('inf')  # Iniciamos com infinito para comparar com o menor preço
continuar = 'S'

# Loop para inserir os produtos
while continuar.upper() == 'S':
    # Entrada de dados do usuário
    nome_produto = input('Digite o nome do produto: ')
    preco_produto = float(input('Digite o preço do produto: R$'))

    # Atualizando o total gasto
    total_gasto += preco_produto

    # Verificando se o produto custa mais de R$1000
    if preco_produto > 1000:
        produtos_acima_1000 += 1

    # Verificando se o produto é o mais barato
    if preco_produto < preco_produto_mais_barato:
        preco_produto_mais_barato = preco_produto
        produto_mais_barato = nome_produto

    # Perguntando ao usuário se deseja continuar
    continuar = input('Deseja adicionar mais produtos? [S/N]: ').strip()

# Exibindo o resumo da compra
print('\n======= RESUMO DA COMPRA =======')
print(f'Total gasto: R${total_gasto:.2f}')
print(f'Quantidade de produtos que custam mais de R$1000: {produtos_acima_1000}')
print(f'O produto mais barato foi: {produto_mais_barato} que custa R${preco_produto_mais_barato:.2f}')


