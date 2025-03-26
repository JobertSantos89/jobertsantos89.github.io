import db

def listar(ativo=True):
    """ Retorna todos os professores cadastrados, filtrando ativos ou inativos """
    with db.conn.cursor() as cursor:
        sql = '''
            SELECT id, nome, registro, fl_ativo, criado_em
            FROM professores
            WHERE fl_ativo = %s
        '''
        cursor.execute(sql, (ativo,))
        return cursor.fetchall()

def cadastrar(nome: str, registro: str):
    """ Cadastra um novo professor """
    with db.conn.cursor() as cursor:
        sql = '''
            INSERT INTO professores (nome, registro, fl_ativo)
            VALUES (%s, %s, True)
        '''
        cursor.execute(sql, (nome, registro))
    db.conn.commit()

def atualizar(professor_id: int, nome: str, registro: str):
    """ Atualiza os dados do professor """
    with db.conn.cursor() as cursor:
        sql = '''
            UPDATE professores
            SET nome = %s, registro = %s
            WHERE id = %s
        '''
        cursor.execute(sql, (nome, registro, professor_id))
    db.conn.commit()

def desativar(professor_id: int):
    """ Desativa um professor (fl_ativo = False) """
    with db.conn.cursor() as cursor:
        sql = '''
            UPDATE professores
            SET fl_ativo = False
            WHERE id = %s
        '''
        cursor.execute(sql, (professor_id,))
    db.conn.commit()

def ativar(professor_id: int):
    """ Ativa um professor (fl_ativo = True) """
    with db.conn.cursor() as cursor:
        sql = '''
            UPDATE professores
            SET fl_ativo = True
            WHERE id = %s
        '''
        cursor.execute(sql, (professor_id,))
    db.conn.commit()
