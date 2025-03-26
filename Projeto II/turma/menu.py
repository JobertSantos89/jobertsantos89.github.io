import turma.repository as turma_repository
import professor.repository as professor_repository
import materia.repository as materia_repository

def run():
    while True:
        print('=== Gerenciamento de Turmas ===')
        print('[1] - Listar Turmas')
        print('[2] - Cadastrar Turma')
        print('[3] - Atualizar Turma')
        print('[4] - Excluir Turma')
        print('[5] - Voltar')

        opcao = input('Digite a opção desejada: ')

        if opcao == '1':
            turmas = turma_repository.listar()
            print(' Turmas Cadastradas '.center(50, '-'))
            for id, materia_id, professor_id, data_inicio, data_fim, horario, duracao, dia_da_semana in turmas:
                print(f'[{id}] - Matéria: {materia_id} | Professor: {professor_id} | Início: {data_inicio}')
            print('-' * 50)

        elif opcao == '2':
            materia_id = int(input('ID da matéria: '))
            professor_id = int(input('ID do professor: '))
            data_inicio = input('Data de início (dd/mm/aaaa): ')
            data_fim = input('Data de fim (dd/mm/aaaa): ')
            horario = input('Horário: ')
            duracao = input('Duração: ')
            dia_da_semana = input('Dia da semana: ')
            turma_repository.cadastrar(materia_id, professor_id, data_inicio, data_fim, horario, duracao, dia_da_semana)

        elif opcao == '3':
            turma_id = int(input('ID da turma: '))
            materia_id = int(input('Novo ID da matéria: '))
            professor_id = int(input('Novo ID do professor: '))
            data_inicio = input('Nova data de início (dd/mm/aaaa): ')
            data_fim = input('Nova data de fim (dd/mm/aaaa): ')
            horario = input('Novo horário: ')
            duracao = input('Nova duração: ')
            dia_da_semana = input('Novo dia da semana: ')
            turma_repository.atualizar(turma_id, materia_id, professor_id, data_inicio, data_fim, horario, duracao, dia_da_semana)

        elif opcao == '4':
            turma_id = int(input('ID da turma: '))
            turma_repository.excluir(turma_id)

        elif opcao == '5':
            break

        else:
            print('Opção Inválida.')

if __name__ == '__main__':
    run()
