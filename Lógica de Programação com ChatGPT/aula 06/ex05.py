from getpass import getpass

# O Banco de Dados
usuario_cadastrado = 'davi.lucciola'
senha_cadastrada = '0123'

# Tentativa de Login
usuario = input('Usuário: ')
senha = getpass('Senha: ') # É um input que não mostra o que está sendo digitado

if usuario == usuario_cadastrado and senha == senha_cadastrada:
    print(f'Seja bem vindo {usuario_cadastrado}')
else:
    print('Usuário ou senha inválidos.')