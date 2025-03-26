import mysql.connector

# Conectar ao banco de dados MySQL
conn = mysql.connector.connect(
    host='127.0.0.1',  # Endereço IP do MySQL (localhost)
    user='root',  # Seu nome de usuário do MySQL
    password='',  # Sua senha do MySQL
    database='escola',  # O nome do banco de dados
    port=3306  # Porta padrão do MySQL
)


def criar_tabelas():
    """ Cria as tabelas no banco de dados, caso não existam """
    with conn.cursor() as cursor:
        # Criação da tabela 'alunos'
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS alunos (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                idade INT NOT NULL
            )
        ''')

        # Criação da tabela 'materias'
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS materias (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                codigo VARCHAR(10) NOT NULL,
                descricao TEXT
            )
        ''')

        # Criação da tabela 'Professores'
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS professores (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                idade INT NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS materias (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                codigo VARCHAR(10) NOT NULL,
                descricao TEXT
            )
        ''')

        # Criação da tabela 'turmas'
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS turmas (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                materia_id INT REFERENCES materias(id),
                ano INT NOT NULL
            )
        ''')

        # Confirma a execução dos comandos
        conn.commit()

# Chama a função para criar as tabelas
criar_tabelas()
