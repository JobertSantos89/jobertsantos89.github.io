# Ex03. Faça um programa que peça o nome, 3 notas de um aluno, e armazene-os em um dicionário, também armazene nesse dicionário a média e a situação do aluno (>= 6 está aprovado, se não reprovado.)

# # Passo 1: Solicitar o nome e as notas do aluno
# nome = input('Digite o nome do aluno: ')
# nota1 = float(input('Digite a primeira nota do aluno: '))
# nota2 = float(input('Digite a segunda nota do aluno: '))
# nota3 = float(input('Digite a terceira nota do aluno: '))


# # Passo 2: Calcular a média
# media = (nota1 + nota2 + nota3) / 3

# # Passo 3: Determinar a situação do aluno
# if media >= 6:
#     situacao = 'Aprovado'
# else:
#     situacao = 'Reprovado'

# # Passo 4: Armazenar as informações em um dicionário
# aluno = {
#     'nome': nome,                  # Nome do aluno
#     'notas': [nota1, nota2, nota3], # Lista com as 3 notas
#     'media': media,                # Média calculada
#     'situacao': situacao           # Situação do aluno (Aprovado ou Reprovado)
# }

# # Passo 5: Exibir o conteúdo do dicionário
# print("\nInformações do Aluno:")
# print(aluno)

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