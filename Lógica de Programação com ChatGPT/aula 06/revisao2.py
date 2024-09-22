aluno = input('Digite o nome do aluno: ')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = (nota1 + nota2 + nota3) / 3

if media >= 6:
    situacao = 'Aprovado'
elif media >= 4 and media < 6:
    situacao = 'Em Recuperação'
elif media >= 4 and media < 6:
    situacao = 'Em Recuperação'
elif media >= 4 and media < 6:
    situacao = 'Em Recuperação'
else:
    situacao = 'Reprovado'

print('-' * 5 + ' BOLETIM ' + '-' * 5)
print(f'NOME: {aluno}')
print(f'MEDIA: {media:.2f}')
print(f'SITUAÇÃO: {situacao}')