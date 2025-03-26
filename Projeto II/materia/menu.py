import materia.repository as materia_repo

def listar_materias():
    materias = materia_repo.listar_materias()
    if materias:
        print('Lista de Matérias:')
        for materia in materias:
            print(f'ID: {materia[0]} | Nome: {materia[1]} | Carga Horária: {materia[2]}')
    else:
        print('Nenhuma matéria encontrada.')

def adicionar_materia():
    nome = input('Nome da matéria: ')
    carga_horaria = input('Carga horária da matéria: ')
    materia_repo.adicionar_materia(nome, carga_horaria)
    print(f'Matéria {nome} adicionada com sucesso!')

def editar_materia():
    materia_id = input('Digite o ID da matéria a ser editada: ')
    materia = materia_repo.obter_materia_por_id(materia_id)
    if materia:
        print(f'Editando a matéria {materia[1]}')
        nome = input(f'Novo nome ({materia[1]}): ') or materia[1]
        carga_horaria = input(f'Nova carga horária ({materia[2]}): ') or materia[2]
        materia_repo.editar_materia(materia_id, nome, carga_horaria)
        print(f'Matéria {nome} atualizada com sucesso!')
    else:
        print('Matéria não encontrada.')

def run():
    while True:
        print('=== Gerenciamento de Matérias ===')
        print('[1] - Listar Matérias')
        print('[2] - Adicionar Matéria')
        print('[3] - Editar Matéria')
        print('[4] - Voltar')

        opcao = input('Digite a opção desejada: ')

        if opcao == '1':
            listar_materias()
        elif opcao == '2':
            adicionar_materia()
        elif opcao == '3':
            editar_materia()
        elif opcao == '4':
            break
        else:
            print('Opção Inválida.')
