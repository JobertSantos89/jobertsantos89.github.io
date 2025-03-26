import aluno.menu
import professor.menu
import turma.menu
import materia.menu

def menu():
    while True:
        print('===== Gerenciamento da Escola =====')
        print('[1] - Modulo de Materias')
        print('[2] - Modulo de Professores')
        print('[3] - Modulo de Alunos')
        print('[4] - Modulo de Turmas')
        print('[5] - Sair')

        opcao = input('Digite qual opção deseja: ')

        if opcao == '1':
            materia.menu.run()  # Chama o menu de matérias
        elif opcao == '2':
            professor.menu.run()  # Chama o menu de professores
        elif opcao == '3':
            aluno.menu.run()  # Chama o menu de alunos
        elif opcao == '4':
            turma.menu.run()  # Chama o menu de turmas
        elif opcao == '5':
            break
        else:
            print('Opção Inválida.')

if __name__ == '__main__':
    menu()
