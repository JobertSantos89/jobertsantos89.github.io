# Estruturas de Repetição (For)
# O for é uma estrutura de repetição utilizada para 
# percorrer uma quantidade de valores pre definida.
# Ele percorre uma sequência (íteraveis), e para cada valor da sequencia ele executa o seu bloco de codigo

# Exemplo 1:
# Repetir 10 vezes, começando de 0, até 9, pulando de 1 em 1
for numero in range(0, 10, 1):
    print(numero)

print('Fim exemplo 1.')
# A função "range" gera para gente uma sequencia numerica
# onde o primeiro valor é o valor de inicio (incluso), o segundo valor é o valor de parada (excluso) e o terceiro valor é o passo.

# Exemplo 2:
# Repetir 10 vezes, começando de 1, até 10, pulando de 1 em 1
valor_final = 10
for numero in range(1, valor_final + 1):
    print(numero)

print('Fim exemplo 2.')

# Exemplo 3:
# Repetir 5 vezes, começando de 0, até 5, pulando de 1 em 1
for numero in range(5):
    print(numero)

print('Fim exemplo 2.')
