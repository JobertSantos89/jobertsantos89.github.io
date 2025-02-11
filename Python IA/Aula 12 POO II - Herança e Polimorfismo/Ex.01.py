import math

class Forma:
    """Classe base para formas geométricas"""
    def calcular_area(self):
        pass  # Método abstrato

    def calcular_perimetro(self):
        pass  # Método abstrato

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * self.raio ** 2  # Área do círculo: πr²

    def calcular_perimetro(self):
        return 2 * math.pi * self.raio  # Perímetro do círculo: 2πr

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura  # Área do retângulo: base × altura

    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)  # Perímetro do retângulo: 2(base + altura)

# Criando objetos das classes derivadas
circulo = Circulo(5)
retangulo = Retangulo(4, 6)

# Exibindo resultados
print(f"Área do círculo: {circulo.calcular_area():.2f}")
print(f"Perímetro do círculo: {circulo.calcular_perimetro():.2f}")

print(f"Área do retângulo: {retangulo.calcular_area():.2f}")
print(f"Perímetro do retângulo: {retangulo.calcular_perimetro():.2f}")
