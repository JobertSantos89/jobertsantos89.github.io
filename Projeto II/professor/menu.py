import professor.repository as professor_repository

def run():
    while True:
        print('=== Gerenciamento de Professores ===')
        print('[1] - Listar Professores Ativos')
        print('[2] - Listar Professores Inativos')
        print('[3] - Cadastrar Professor')
        print('[4] - Atualizar Professor')
        print('[5] - Desativar Professor')
        print('[6] - Ativar Professor')
        print('[7] - Voltar')

        opcao = input('Digite a opção desejada: ')

        if opcao == '1':
            professores = professor_repository.listar(ativo=True)
            print(' Professores Ativos '.center(50, '-'))
            for id, nome, registro, fl_ativo, criado_em in professores:
                print(f'[{id}] - {nome} - {registro} - Criado em: {criado_em}')
            print('-' * 50)

        elif opcao == '2':
            professores = professor_repository.listar(ativo=False)
            print(' Professores Inativos '.center(50, '-'))
            for id, nome, registro, fl_ativo, criado_em in professores:
                print(f'[{id}] - {nome} - {registro} - Criado em: {criado_em}')
            print('-' * 50)

        elif opcao == '3':
            nome = input('Nome do professor: ')
            registro = input('Registro do professor: ')
            professor_repository.cadastrar(nome, registro)

        elif opcao == '4':
            professor_id = int(input('ID do professor: '))
            nome = input('Novo nome: ')
            registro = input('Novo registro: ')
            professor_repository.atualizar(professor_id, nome, registro)

        elif opcao == '5':
            professores = professor_repository.listar(ativo=True)
            if not professores:
                print('Não há professores ativos para desativar.')
            else:
                print(' Professores Ativos '.center(50, '-'))
                for id, nome, registro, fl_ativo, criado_em in professores:
                    print(f'[{id}] - {nome} - {registro}')
                print('-' * 50)

                professor_id = int(input('ID do professor a ser desativado: '))
                professor_repository.desativar(professor_id)

        elif opcao == '6':
            professores = professor_repository.listar(ativo=False)
            if not professores:
                print('Não há professores inativos para ativar.')
            else:
                print(' Professores Inativos '.center(50, '-'))
                for id, nome, registro, fl_ativo, criado_em in professores:
                    print(f'[{id}] - {nome} - {registro}')
                print('-' * 50)

                professor_id = int(input('ID do professor a ser ativado: '))
                professor_repository.ativar(professor_id)

        elif opcao == '7':
            break

        else:
            print('Opção Inválida.')

if __name__ == '__main__':
    run()
