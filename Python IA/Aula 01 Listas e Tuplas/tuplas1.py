# Tuplas
aluno1 = ('Lucas', 8.88, 'Aprovado')
aluno2 = ('Pedro', 9, 'Aprovado')

# Desempacotamento
nome, media, situacao = aluno1
print(nome)
print(media)
print(situacao)

# Lista de Tuplas
alunos = [aluno1, aluno2]
print(alunos)

# Iterando Lista de Tuplas
for aluno in alunos:
    print(aluno)

# Desempacotamento Durante a Iteração
for nome, media, situacao in alunos:
    print(nome, media, situacao)
