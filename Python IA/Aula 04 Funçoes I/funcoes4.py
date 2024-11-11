# Funções 4
# Parametros Opcionais são parametros onde definimos um valor padrão, caso o parametro seja passado na função, ele irá considerar o passado, caso não, ele irá considerar o padrão.

def nome_completo(nome: str, ultimo_nome: str, nome_do_meio: str = ''):
    completo = nome

    if nome_do_meio != '':
        completo += f' {nome_do_meio}'

    completo += f' {ultimo_nome}'
    return completo

nome = input('Digite seu nome: ')
meio = input('Digite seu nome do meio: ')
sobrenome = input('Digite seu sobrenome: ')

# Chamando 3 Parametros
completo = nome_completo(nome, sobrenome, meio)

# Chamando sem o ultimo parametro (que contém valor padrão.)
nome_curto = nome_completo(nome, sobrenome)

print(f'Nome Completo: {completo}.')
print(f'Nome Completo: {nome_curto}.')