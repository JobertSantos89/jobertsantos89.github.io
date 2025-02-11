# Classe base
class Veiculo:
    def movimentar(self):
        print("Veículo está em movimento.")

# Subclasse Carro sobrescrevendo o método movimentar
class Carro(Veiculo):
    def movimentar(self):
        print("Carro está dirigindo.")

# Subclasse Moto sobrescrevendo o método movimentar
class Moto(Veiculo):
    def movimentar(self):
        print("Moto está acelerando.")

# Testando as classes
veiculo = Veiculo()
veiculo.movimentar()

carro = Carro()
carro.movimentar()

moto = Moto()
moto.movimentar() 
