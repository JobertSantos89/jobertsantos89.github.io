# Crie uma tupla chamada frutas que contenha três frutas
frutas = ('maçã', 'banana', 'laranja')

# Acesse o segundo elemento da tupla frutas e atribua-o à variável fruta2
fruta2 = frutas[1]

# Tente alterar o valor de um elemento na tupla frutas e observe a exceção gerada
# Exemplo de tentativa inválida: frutas[0] = 'uva'  # Isso gerará um TypeError

# Crie uma segunda tupla chamada outras_frutas com duas frutas diferentes
outras_frutas = ('uva', 'morango')

# Concatene as tuplas frutas e outras_frutas em uma nova tupla chamada todas_as_frutas
todas_as_frutas = frutas + outras_frutas

# Conte quantas vezes a fruta 'banana' aparece na tupla todas_as_frutas
quantidade_bananas = todas_as_frutas.count('banana')

# Crie uma tupla chamada ponto que represente coordenadas (x, y)
ponto = (10, 20)

# Use o desempacotamento para atribuir os valores a variáveis coord_x e coord_y
coord_x, coord_y = ponto

# Crie uma função chamada informacoes_pessoa que retorna uma tupla contendo o nome, idade e profissão de uma pessoa
def informacoes_pessoa():
    return ('João', 25, 'Engenheiro')

# Desempacote a tupla ao chamar a função e atribua os valores a variáveis adequadas
nome, idade, profissao = informacoes_pessoa()

# Imprima os resultados
print("Segunda fruta:", fruta2)
print("Quantidade de bananas:", quantidade_bananas)
print("Coordenadas:", coord_x, coord_y)
print("Informações da pessoa:", nome, idade, profissao)