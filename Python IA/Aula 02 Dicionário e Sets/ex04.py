# Ex04. Faça um programa para realizar uma votação que será armazenada em um dicionário, onde os candidatos são as chaves, e o valor é a quantidade de votos. O programa iniciará com os candidatos preenchidos e deverá perguntar quantos votos serão realizados. Ao final mostre o resultado da votação.

# Função para realizar a votação
def realizar_votacao(candidatos, total_votos):
    while total_votos > 0:
        print("\nCandidatos:")
        for numero, candidato in enumerate(candidatos, start=1):
            print(f"{numero} - {candidato}")
        
        try:
            voto = int(input("Digite o número do candidato em que você quer votar: "))

            # Verifica se o número é válido
            if 1 <= voto <= len(candidatos):
                candidato_escolhido = list(candidatos.keys())[voto - 1]
                candidatos[candidato_escolhido] += 1
                total_votos -= 1  # Diminui o número de votos restantes
            else:
                print("Número inválido! Por favor, insira um número válido.")
        except ValueError:
            print("Entrada inválida! Por favor, insira um número.")
    
    return candidatos

# Função para exibir o resultado final da votação
def exibir_resultado(candidatos):
    print("\nResultado da Votação:")
    for candidato, votos in candidatos.items():
        print(f"{candidato}: {votos} voto(s)")

# Programa Principal

# Dicionário com os candidatos e seus votos iniciais (começam com 0)
candidatos = {
    'Candidato A': 0,
    'Candidato B': 0,
    'Candidato C': 0
}

# Pergunta ao usuário quantos votos serão realizados
total_votos = int(input("Quantos votos serão realizados? "))

# Realiza a votação
candidatos = realizar_votacao(candidatos, total_votos)

# Exibe o resultado final
exibir_resultado(candidatos)