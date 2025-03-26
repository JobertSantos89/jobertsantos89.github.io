import db

def listar_alunos():
    """ Retorna todos os alunos cadastrados """
    with db.conn.cursor() as cursor:
        sql = '''
            SELECT id, nome, idade
            FROM alunos
        '''
        cursor.execute(sql)
        return cursor.fetchall()

def cadastrar_aluno(nome: str, idade: int):
    """ Cadastra um novo aluno """
    with db.conn.cursor() as cursor:
        sql = '''
            INSERT INTO alunos (nome, idade)
            VALUES (%s, %s)
        '''
        cursor.execute(sql, (nome, idade))
    db.conn.commit()

def atualizar_aluno(aluno_id: int, nome: str, idade: int):
    """ Atualiza os dados de um aluno """
    with db.conn.cursor() as cursor:
        sql = '''
            UPDATE alunos
            SET nome = %s, idade = %s
            WHERE id = %s
        '''
        cursor.execute(sql, (nome, idade, aluno_id))
    db.conn.commit()

def excluir_aluno(aluno_id: int):
    """ Exclui um aluno """
    with db.conn.cursor() as cursor:
        sql_delete = '''
            DELETE FROM alunos WHERE id = %s
        '''
        cursor.execute(sql_delete, (aluno_id,))
        db.conn.commit()
