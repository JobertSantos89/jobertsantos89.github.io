class Veiculo:
    """Classe base para veículos"""
    def __init__(self):
        self.cor = None
        self.modelo = None

    def set_cor(self, cor):
        self.cor = cor
        return self  # Retorna o próprio objeto para permitir encadeamento

    def set_modelo(self, modelo):
        self.modelo = modelo
        return self  # Retorna o próprio objeto para permitir encadeamento

    def exibir_detalhes(self):
        print(f"Modelo: {self.modelo}, Cor: {self.cor}")

class Carro(Veiculo):
    """Classe derivada representando um carro"""
    def __init__(self):
        super().__init__()  # Chama o construtor da classe base

class Bicicleta(Veiculo):
    """Classe derivada representando uma bicicleta"""
    def __init__(self):
        super().__init__()  # Chama o construtor da classe base

# Criando um carro e configurando seus atributos com encadeamento de métodos
carro = Carro().set_modelo("Sedan").set_cor("Preto")
bicicleta = Bicicleta().set_modelo("Mountain Bike").set_cor("Vermelha")

# Exibindo detalhes dos veículos
carro.exibir_detalhes()
bicicleta.exibir_detalhes()
