#ATIVIDADE PRÁTICA
#Considere uma lista que representa a pontuação de alunos em uma turma:
#pontuacao_alunos = [75, 92, 84, 65, 78, 90, 88, 70, 95, 82]
#Acesse e imprima a pontuação do terceiro aluno na lista.
#O professor decidiu adicionar 5 pontos à pontuação do quarto aluno.
#Faça essa modificação na lista.
#Crie uma nova lista chamada pontuacao_dobrada duplicando a
#pontuação de cada aluno.
#Utilize a função len( ) para determinar o número total de alunos na turma.
#Encontre e imprima a pontuação máxima e mínima na lista.
#Utilize um loop for para imprimir a pontuação de cada aluno na lista.
#Ordene a lista de pontuações em ordem decrescente.
#Crie uma nova lista chamada pontuacao_reversa que contenha a
#pontuação dos alunos na ordem inversa.
#Atividade solucionada em Python:

# Pontuação dos alunos
pontuacao_alunos = [75, 92, 84, 65, 78, 90, 88, 70, 95, 82]

# Acesse e imprima a pontuação do terceiro aluno na lista
print("Pontuação do terceiro aluno:", pontuacao_alunos[2])

# Adicione 5 pontos à pontuação do quarto aluno
pontuacao_alunos[3] += 5

# Crie uma nova lista chamada pontuacao_dobrada duplicando a pontuação de cada aluno
pontuacao_dobrada = [pontuacao * 2 for pontuacao in pontuacao_alunos]

# Use a função len() para determinar o número total de alunos na turma
numero_alunos = len(pontuacao_alunos)
print("Número total de alunos:", numero_alunos)

# Encontre e imprima a pontuação máxima e mínima na lista
pontuacao_maxima = max(pontuacao_alunos)
pontuacao_minima = min(pontuacao_alunos)
print("Pontuação máxima:", pontuacao_maxima)
print("Pontuação mínima:", pontuacao_minima)

# Use um loop for para imprimir a pontuação de cada aluno na lista
print("Pontuações dos alunos:")
for pontuacao in pontuacao_alunos:
    print(pontuacao)

# Ordene a lista de pontuações em ordem decrescente
pontuacao_alunos.sort(reverse=True)

# Crie uma nova lista chamada pontuacao_reversa que contenha a pontuação dos alunos na ordem inversa
pontuacao_reversa = pontuacao_alunos.copy()

# Imprima a lista ordenada em ordem decrescente
print("Pontuações ordenadas em ordem decrescente:", pontuacao_alunos)

# Imprima a lista reversa
pontuacao_reversa.reverse()
print("Pontuações na ordem inversa:", pontuacao_reversa)