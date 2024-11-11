def nome_completo(nome: str, sobrenome: str):
    return f'{nome} {sobrenome}'

nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome (Opcional): ')

completo = nome_completo(nome, sobrenome)

print(f'Nome: {completo}.')