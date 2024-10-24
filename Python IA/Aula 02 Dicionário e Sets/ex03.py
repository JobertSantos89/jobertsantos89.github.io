# Ex03. Faça um programa que peça o nome, 3 notas de um aluno, e armazene-os em um dicionário, também armazene nesse dicionário a média e a situação do aluno (>= 6 está aprovado, se não reprovado.)

aluno = {}

aluno['nome'] = input('Digite o nome do aluno: ')
aluno['notas'] = []

for i in range(3):
    nota = float(input(f'Digite a {i + 1}º nota: '))
    aluno['notas'].append(nota)

aluno['media'] = sum(aluno['notas']) / len(aluno['notas'])
aluno['situacao'] = 'Aprovado' if aluno['media'] >= 6 else 'Reprovado'

print('======= BOLETIM =======')
print(f'Aluno: {aluno.get('nome')}')
print(f'Notas: {aluno.get('notas')}')
print(f'Média: {aluno.get('media'):.2f}')
print(f'Situacao: {aluno.get('situacao')}')