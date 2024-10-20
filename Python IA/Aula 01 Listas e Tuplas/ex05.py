# Ex05. Faça um programa que peça nome e categoria de N produtos (o usuário irá determinar quando ele irá parar de cadastrar), ao finalizar os cadastros, mostre o nome e categorias registradas para todos os produtos.

produtos = []

print('======= Loja do Brabo ======')
while True:
    resp = input('Deseja cadastrar um novo produto [S/N]? -> ').upper()

    if resp not in ('S', 'N'):
        print('Entrada inválida, Digite novamente.')
        continue

    if resp == 'N':
        break

    nome = input('Digite o nome do produto: ')
    categoria = input('Digite a categoria do produto: ')

    produto = (nome, categoria)
    produtos.append(produto)


print('======= Produtos ======')
for nome, categoria in produtos:
    print(f'- {nome} ({categoria})')