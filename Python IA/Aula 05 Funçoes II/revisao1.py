# Revisão Funções 1

# def <nome_funcao>(...<parametros>):
#   ... # Corpo da função

def somar(a, b, c):
    resultado = a + b + c
    return resultado


# Chamando a Função
# Exemplo 1
n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
n3 = int(input('Digite o 3º valor: '))

soma = somar(n1, n2, n3)
print(f'Primeira Chamada: {soma}')

# Exemplo 2
valor = somar(3, 6, 7)
print(f'Segunda Chamada: {valor}')