from banco_infinity.banco import Banco
from banco_infinity.view import BancoView

def main():
    banco = Banco()  # Criando uma instância do Banco
    banco_view = BancoView(banco)  # Criando a interface do banco
    banco_view.run()  # Executando o menu principal

if __name__ == "__main__":
    main()