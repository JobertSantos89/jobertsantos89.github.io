# Inicializando o dicionário para armazenar produtos e preços
produtos = {}

# Laço para solicitar o nome e preço dos cinco produtos
for i in range(5):
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    produtos[nome] = preco  # Armazena o produto como chave e o preço como valor

# Calculando o valor total da compra
valor_total = sum(produtos.values())

# Exibindo o valor total da compra
print(f"\nValor total da compra: R${valor_total:.2f}")
