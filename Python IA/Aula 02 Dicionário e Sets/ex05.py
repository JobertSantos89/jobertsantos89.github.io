# Ex05. Faça um programa para cadastrar 3 cursos que serão armazenados em um dicionário onde o nome do curso será a chave, e o valor será outro dicionário contendo "nivel" e "duração"
# Exemplo:

# cursos = {
#     'Python': {
#         'nivel': 2,
#         'duracao': 5
#     },
#     'Javascript': {
#         'nivel': 3,
#         'duracao': 7
#     },
#     'Java': {
#         'nivel': 5,
#         'duracao': 10
#     }
# }   


# Função para cadastrar cursos
def cadastrar_cursos(num_cursos):
    cursos = {}

    for i in range(num_cursos):
        nome_curso = input(f"Digite o nome do {i+1}º curso: ").strip()
        nivel = int(input(f"Digite o nível do curso {nome_curso} (1 a 5): "))
        duracao = int(input(f"Digite a duração (em meses) do curso {nome_curso}: "))

        # Armazena os dados do curso em um dicionário
        cursos[nome_curso] = {
            'nível': nivel,
            'duração': duracao
        }
        print(f"Curso '{nome_curso}' cadastrado com sucesso!\n")

    return cursos

# Função para exibir os cursos cadastrados
def exibir_cursos(cursos):
    print("\nCursos Cadastrados:")
    for curso, detalhes in cursos.items():
        print(f"Curso: {curso}")
        print(f"  Nível: {detalhes['nível']}")
        print(f"  Duração: {detalhes['duração']} meses\n")

# Programa Principal
num_cursos = 3  # Número de cursos a serem cadastrados

# Cadastrar os cursos
cursos = cadastrar_cursos(num_cursos)

# Exibir os cursos cadastrados
exibir_cursos(cursos)
