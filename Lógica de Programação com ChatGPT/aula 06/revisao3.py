soma = 0
aluno = input('Digite o nome do aluno: ')
qtd_notas = int(input('Quantas notas deseja inserir?'))

for n in range(qtd_notas):
    while True:
        nota = input(f'Digite a {n + 1}º nota: ').replace(',', '.')

        if nota.replace('.', '').isnumeric():
            break

        print('Nota Inválida! Digite Novamente!')
    soma += float(nota)

media = soma / qtd_notas

if media >= 6:
    situacao = 'Aprovado'
elif media >= 4 and media < 6:
    situacao = 'Em Recuperação'
else:
    situacao = 'Reprovado'

print('-------------------')
print('-' * 5 + ' BOLETIM ' + '-' * 5)
print(f'NOME: {aluno}')
print(f'MEDIA: {media:.2f}')
print(f'SITUAÇÃO: {situacao}')
print('-------------------')
