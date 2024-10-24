# Sistema de Cadastro de Alunos - Expansão com múltiplos alunos e salvamento em arquivo

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

def exibir_alunos(alunos):
    print("\nLista de Alunos Cadastrados:")
    for i, aluno in enumerate(alunos, 1):
        print(f"\nAluno {i}:")
        print(f"Nome: {aluno['nome']}")
        print(f"Idade: {aluno['idade']} anos")
        print(f"Notas: Matemática: {aluno['notas'][0]}, Ciências: {aluno['notas'][1]}, História: {aluno['notas'][2]}")
    print("\n")

def salvar_alunos_em_arquivo(alunos, nome_arquivo="alunos_cadastrados.txt"):
    with open(nome_arquivo, 'w') as arquivo:
        for aluno in alunos:
            arquivo.write(f"Nome: {aluno['nome']}\n")
            arquivo.write(f"Idade: {aluno['idade']} anos\n")
            arquivo.write(f"Notas: Matemática: {aluno['notas'][0]}, Ciências: {aluno['notas'][1]}, História: {aluno['notas'][2]}\n")
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

# Exibir a lista de todos os alunos cadastrados
exibir_alunos(alunos)

# Salvar os dados em um arquivo
salvar_alunos_em_arquivo(alunos)
