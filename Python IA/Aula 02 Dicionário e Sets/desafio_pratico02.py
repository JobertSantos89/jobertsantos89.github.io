# Sistema de Cadastro de Alunos - Passo 2

# Função para cadastrar um aluno
def cadastrar_aluno():
    # Solicitar o nome e a idade do aluno
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))

    # Solicitar as notas de três disciplinas
    matematica = float(input("Digite a nota em Matemática: "))
    ciencias = float(input("Digite a nota em Ciências: "))
    historia = float(input("Digite a nota em História: "))

    # Armazenar as notas em uma tupla
    notas = (matematica, ciencias, historia)

    # Armazenar os dados do aluno em um dicionário
    aluno = {
        'nome': nome,
        'idade': idade,
        'notas': notas
    }

    return aluno

# Função para calcular a média das notas de um aluno
def calcular_media(notas):
    return sum(notas) / len(notas)

# Função para exibir todos os alunos cadastrados, junto com a média de cada um
def exibir_alunos_com_medias(alunos):
    print("\nLista de Alunos Cadastrados com Médias:")
    for i, aluno in enumerate(alunos, 1):
        media = calcular_media(aluno['notas'])
        print(f"\nAluno {i}:")
        print(f"Nome: {aluno['nome']}")
        print(f"Idade: {aluno['idade']} anos")
        print(f"Notas: Matemática: {aluno['notas'][0]}, Ciências: {aluno['notas'][1]}, História: {aluno['notas'][2]}")
        print(f"Média: {media:.2f}")
    print("\n")

# Função para encontrar o aluno com a melhor média
def aluno_com_melhor_media(alunos):
    if not alunos:
        return None

    melhor_aluno = alunos[0]
    melhor_media = calcular_media(melhor_aluno['notas'])

    for aluno in alunos[1:]:
        media_atual = calcular_media(aluno['notas'])
        if media_atual > melhor_media:
            melhor_aluno = aluno
            melhor_media = media_atual

    return melhor_aluno, melhor_media

# Função para salvar os alunos cadastrados em um arquivo
def salvar_alunos_em_arquivo(alunos, nome_arquivo="alunos_cadastrados.txt"):
    with open(nome_arquivo, 'w') as arquivo:
        for aluno in alunos:
            media = calcular_media(aluno['notas'])
            arquivo.write(f"Nome: {aluno['nome']}\n")
            arquivo.write(f"Idade: {aluno['idade']} anos\n")
            arquivo.write(f"Notas: Matemática: {aluno['notas'][0]}, Ciências: {aluno['notas'][1]}, História: {aluno['notas'][2]}\n")
            arquivo.write(f"Média: {media:.2f}\n")
            arquivo.write("\n")
    print(f"Dados dos alunos foram salvos no arquivo '{nome_arquivo}'.")

# Lista para armazenar todos os alunos
alunos = []

# Laço para permitir o cadastro de múltiplos alunos
while True:
    # Cadastrar um aluno
    aluno = cadastrar_aluno()
    alunos.append(aluno)

    # Perguntar se o usuário quer continuar cadastrando
    continuar = input("Deseja cadastrar outro aluno? (s/n): ").strip().lower()
    if continuar != 's':
        break

# Exibir todos os alunos cadastrados com as suas médias
exibir_alunos_com_medias(alunos)

# Identificar e exibir o aluno com a melhor média
melhor_aluno, melhor_media = aluno_com_melhor_media(alunos)
if melhor_aluno:
    print(f"Aluno com a Melhor Média:")
    print(f"Nome: {melhor_aluno['nome']}")
    print(f"Média: {melhor_media:.2f}")

# Salvar os dados em um arquivo
salvar_alunos_em_arquivo(alunos)
