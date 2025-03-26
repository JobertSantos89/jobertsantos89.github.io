import db

def listar_materias():
    conn = db.conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM materias')
    materias = cursor.fetchall()
    conn.close()
    return materias

def adicionar_materia(nome, carga_horaria):
    conn = db.conectar()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO materias (nome, carga_horaria) VALUES (?, ?)', (nome, carga_horaria))
    conn.commit()
    conn.close()

def editar_materia(materia_id, nome, carga_horaria):
    conn = db.conectar()
    cursor = conn.cursor()
    cursor.execute('UPDATE materias SET nome = ?, carga_horaria = ? WHERE id = ?', (nome, carga_horaria, materia_id))
    conn.commit()
    conn.close()

def obter_materia_por_id(materia_id):
    conn = db.conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM materias WHERE id = ?', (materia_id,))
    materia = cursor.fetchone()
    conn.close()
    return materia
