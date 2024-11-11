# Funções 2
# Para definir uma função precisamos utilizar a palavra reservada "def"

# A função é composta por:
# - Parametros (Entrada)
# - Corpo da Função (Processamento)
# - Retorno (Saída)

# Exemplo:

# Type Hint -> Dica de Tipo
# OBS: O type hint não é obrigatório. 
def saudacao(nome: str) -> str:
    return f'Olá {nome}, Seja bem vindo!'

def boas_vindas(mensagem: str) -> None:
    print(f'BOAS VINDAS: {mensagem}')

# Utilizando a função
nome = input('Digite seu nome: ')

# Chamando a função Saudação, passando nome como parametro.
mensagem_saudacao = saudacao(nome)

# Aqui teremos 2 Prints, um da função "boas vindas", 
# o outro é o retorno da função boas vindas (None, poque não foi especificado retorno) 
print(boas_vindas(mensagem_saudacao)) 
