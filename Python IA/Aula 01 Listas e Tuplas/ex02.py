# Ex02. Faça um programa que começe criando uma lista vazia, e adicione 3 nomes com o "append" utilizando o FOR

nomes = []

for n in range(3):
    nome = input(f'Digite o {n + 1}º nome: ')
    nomes.append(nome)

print(nomes)