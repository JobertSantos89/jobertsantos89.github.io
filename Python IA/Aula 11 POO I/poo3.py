class INSS:
    taxa = 0.1

    def calcular(self, valor: float):
        return valor * self.taxa
    
total = 500
total = total - INSS().calcular(total)