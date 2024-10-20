# Ex02. Faça um programa que peça o nome, raça e cor de um animal e armazene as informações em um dicionário. Ao final mostre os valores nas chaves do dicionário.

animal = {} #Dicionário.

animal['nome'] = input('Digite o nome do animal: ')
animal['raca'] = input('Digite a raça do animal: ')
animal['cor'] = input('Digite a cor do animal: ')

print('Dados do animal: ')
print(f'- Nome: {animal.get("nome")}')
print(f'- Raça: {animal.get("raca")} ({animal["cor"]})')
