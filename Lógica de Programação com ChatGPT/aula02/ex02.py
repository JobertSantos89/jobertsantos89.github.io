# Ex02. Faça um programa que peça o nome e 3 notas de um aluno, 
# ao final mostre o nome e sua média.

# Entrada
print('---- Escolinha Girafales ----')

aluno = input('Digite o nome do aluno: ')

nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))
nota3 = float(input('Digite a 3ª nota: '))

# Processamento
media = (nota1 + nota2 + nota3) / 3

# Saida
print(f'A media do aluno {aluno} é {round(media, 1)}')
print(f'A media do aluno {aluno} é {media:.1f}')