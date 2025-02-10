from tinydb import TinyDB

tarefas = TinyDB('./db.json', indent=2).table('tarefas')

def listar_tarefas():
    return [
        {'id': int(tarefa.doc_id), **tarefa} 
        for tarefa in tarefas.all()
    ]

def atualizar_tarefa(id: int, tarefa_editada: dict):
    tarefa = tarefas.get(doc_id=id)

    if tarefa is None:
        raise RuntimeError('Tarefa não encontrada.')
    
    tarefas.update(tarefa_editada, doc_ids=[id])

def excluir_tarefa(id: int):
    tarefas.remove(doc_ids=[id])

def cadastrar_tarefa(tarefa: dict):
    tarefas.insert(tarefa)
