import os

def listar_arquivos_pastas():
    
    # Obtendo o diretório atual onde o script está sendo executado
    diretorio_atual = os.getcwd()
    
    # Usando a função listdir para obter todos os arquivos e pastas
    itens = os.listdir(diretorio_atual)

    # Exibindo cada item encontrado
    print(f"Arquivos e pastas no diretório '{diretorio_atual}':")
    for item in itens:
        print(item)

if __name__ == "__main__":
    listar_arquivos_pastas()
