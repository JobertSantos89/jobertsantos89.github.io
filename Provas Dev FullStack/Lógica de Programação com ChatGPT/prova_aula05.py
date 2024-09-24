# Função principal
def calcular_medias_turma():
    # Solicitar o número de alunos
    num_alunos = int(input("Digite o número de alunos: "))

    # Inicializando variáveis para armazenar a soma das médias
    soma_medias = 0

    # Loop para iterar sobre o número de alunos
    for i in range(num_alunos):
        print(f"\nAluno {i + 1}:")
        
        # Coletar o nome do aluno
        nome = input("Digite o nome do aluno: ")
        
        # Coletar as três notas
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        nota3 = float(input("Digite a terceira nota: "))
        
        # Calcular a média
        media = (nota1 + nota2 + nota3) / 3
        
        # Adicionar a média do aluno à soma das médias
        soma_medias += media
        
        # Verificar se o aluno foi aprovado ou reprovado
        if media >= 7.0:
            status = "Aprovado"
        else:
            status = "Reprovado"
        
        # Exibir os dados do aluno
        print(f"\nNome: {nome}")
        print(f"Notas: {nota1}, {nota2}, {nota3}")
        print(f"Média: {media:.2f}")
        print(f"Status: {status}")
    
    # Calcular a média geral da turma
    media_geral = soma_medias / num_alunos
    print(f"\nMédia geral da turma: {media_geral:.2f}")

# Chamada da função principal
calcular_medias_turma()

