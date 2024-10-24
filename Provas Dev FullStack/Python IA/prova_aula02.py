# Crie um dicionário que irá armazenar informações de um contato, incluindo o nome, o telefone e o email. 
# Peça ao usuário para fornecer esses dados, solicitando que ele insira o nome do contato, o número de telefone e o endereço de email. 
# Após coletar todas as informações necessárias, exiba o conteúdo do dicionário, mostrando todas as informações do contato inserido pelo usuário.

contato = {}

contato['nome'] = input('Digite o nome do contato: ')
contato['telefone'] = input('Digite o número do telefone do contato: ')
contato['e-mail'] = input('Digite o endereço de e-mail do contato: ')

print('======= CONTATO =======')
print(f"Nome do contato: {contato.get('nome')}")
print(f"Telefone do contato: {contato.get('telefone')}")
print(f"E-mail do contato: {contato.get('e-mail')}")