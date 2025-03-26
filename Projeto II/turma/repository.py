import db

def listar():
    """ Retorna todas as turmas cadastradas """
    with db.conn.cursor() as cursor:
        sql = '''
            SELECT id, materia_id, professor_id, data_inicio, data_fim, horario, duracao, dia_da_semana
            FROM turmas
        '''
        cursor.execute(sql)
        return cursor.fetchall()

def cadastrar(materia_id: int, professor_id: int, data_inicio: str, data_fim: str, horario: str, duracao: str, dia_da_semana: str):
    """ Cadastra uma nova turma """
    with db.conn.cursor() as cursor:
        sql = '''
            INSERT INTO turmas (materia_id, professor_id, data_inicio, data_fim, horario, duracao, dia_da_semana)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        '''
        cursor.execute(sql, (materia_id, professor_id, data_inicio, data_fim, horario, duracao, dia_da_semana))
    db.conn.commit()

def atualizar(turma_id: int, materia_id: int, professor_id: int, data_inicio: str, data_fim: str, horario: str, duracao: str, dia_da_semana: str):
    """ Atualiza os dados de uma turma """
    with db.conn.cursor() as cursor:
        sql = '''
            UPDATE turmas
            SET materia_id = %s, professor_id = %s, data_inicio = %s, data_fim = %s, horario = %s, duracao = %s, dia_da_semana = %s
            WHERE id = %s
        '''
        cursor.execute(sql, (materia_id, professor_id, data_inicio, data_fim, horario, duracao, dia_da_semana, turma_id))
    db.conn.commit()

def excluir(turma_id: int):
    """ Exclui uma turma """
    with db.conn.cursor() as cursor:
        sql = 'DELETE FROM turmas WHERE id = %s'
        cursor.execute(sql, (turma_id,))
    db.conn.commit()
