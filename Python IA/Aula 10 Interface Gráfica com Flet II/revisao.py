import db


nome = input('Digite uma tarefa: ')
data_inicio = input('Digite a data de inicio [dd/MM/yyyy]: ')
data_limite = input('Digite a data limite [dd/MM/yyyy]: ')

nova_tarefa = {
    'nome': nome,
    'data_inicio': data_inicio,
    'data_limite': data_limite
}

db.cadastrar_tarefa(nova_tarefa)

dados = db.listar_tarefas()
print(dados)