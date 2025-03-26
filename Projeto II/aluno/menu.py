import aluno.repository as aluno_repo

def run():
    while True:
        print('=== Gerenciamento de Alunos ===')
        print('[1] - Listar Alunos')
        print('[2] - Cadastrar Aluno')
        print('[3] - Atualizar Aluno')
        print('[4] - Excluir Aluno')
        print('[5] - Voltar')

        opcao = input('Digite a opção desejada: ')

        if opcao == '1':
            alunos = aluno_repo.listar_alunos()  # Chama a função de listar alunos
            if alunos:
                for aluno in alunos:
                    print(f'ID: {aluno[0]} | Nome: {aluno[1]} | Idade: {aluno[2]}')
            else:
                print('Nenhum aluno encontrado.')
        elif opcao == '2':
            nome = input('Digite o nome do aluno: ')
            idade = int(input('Digite a idade do aluno: '))
            aluno_repo.cadastrar_aluno(nome, idade)  # Chama a função de cadastrar aluno
            print(f'Aluno {nome} cadastrado com sucesso!')
        elif opcao == '3':
            aluno_id = int(input('Digite o ID do aluno a ser atualizado: '))
            nome = input('Digite o novo nome do aluno: ')
            idade = int(input('Digite a nova idade do aluno: '))
            aluno_repo.atualizar_aluno(aluno_id, nome, idade)  # Chama a função de atualizar aluno
            print(f'Aluno {aluno_id} atualizado com sucesso!')
        elif opcao == '4':
            aluno_id = int(input('Digite o ID do aluno a ser excluído: '))
            if aluno_repo.excluir_aluno(aluno_id):  # Chama a função de excluir aluno
                print(f'Aluno {aluno_id} excluído com sucesso!')
            else:
                print(f'Não foi possível excluir o aluno {aluno_id}.')
        elif opcao == '5':
            break
        else:
            print('Opção Inválida.')
