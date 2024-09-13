#Você está desenvolvendo um programa em Python para calcular a soma dos números pares dentro de um intervalo determinado pelo usuário. 
#O programa deve solicitar ao usuário que insira dois números inteiros, representando o início e o fim do intervalo (inclusive).
#Utilize um loop 'for' para iterar sobre todos os números no intervalo e somar apenas os números pares. Implemente a estrutura 'else' 
#para exibir uma mensagem indicando que não há números pares no intervalo, caso seja o caso.Ao final, exiba a soma dos números pares encontrados.

# Solicitar ao usuário os limites do intervalo
inicio = int(input("Digite o número inicial do intervalo: "))
fim = int(input("Digite o número final do intervalo: "))

# Inicializar a variável que armazenará a soma dos números pares
soma_pares = 0

# Loop for para iterar sobre o intervalo
for numero in range(inicio, fim + 1):
    if numero % 2 == 0:  # Verificar se o número é par
        soma_pares += numero

# Verificar se foi encontrado algum número par e exibir a mensagem adequada
if soma_pares > 0:
    print(f"A soma dos números pares no intervalo é: {soma_pares}")
else:
    print("Não há números pares no intervalo.")
