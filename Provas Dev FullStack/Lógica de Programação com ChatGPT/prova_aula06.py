# Definindo credenciais corretas
usuario_correto = "usuario123"
senha_correta = "senha123"

# Definindo o número máximo de tentativas
max_tentativas = 3

# Loop para permitir até três tentativas de login
for tentativa in range(max_tentativas):
    # Solicitar entrada do usuário
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    # Verificar se as credenciais estão corretas
    if usuario == usuario_correto and senha == senha_correta:
        print("Bem-vindo ao sistema!")
        break  # Termina o loop se as credenciais estiverem corretas
    else:
        # Calcular tentativas restantes
        tentativas_restantes = max_tentativas - (tentativa + 1)
        print(f"Credenciais incorretas. Você tem {tentativas_restantes} tentativas restantes.")

# Se o usuário falhar todas as tentativas, exibir mensagem de bloqueio
if tentativas_restantes == 0:
    for _ in range(3):
        print("Acesso bloqueado.")
