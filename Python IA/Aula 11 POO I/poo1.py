# Programação Orientada a Objetos
from datetime import date

# Classes
class Pessoa:
    # Metódo Construtor
    def __init__(self, nome: str, altura: float, data_nascimento: date):
        # Atributos
        self.nome = nome
        self.altura = altura
        self.data_nascimento = data_nascimento

    # Metódos (Funções dentro de Classes)
    def calcular_idade(self) -> int:
        return (date.today() - self.data_nascimento).days // 365

# Objetos
pessoa1 = Pessoa('Ermesson', 1.83, date(1997, 8, 21))
pessoa2 = Pessoa('Ricardo', 1.83, date(1992, 1, 10))

# Acessando atributos dos objetos
print(pessoa1.nome)
print(pessoa2.nome)

# Chamar Metódos
print(pessoa1.calcular_idade())
print(pessoa2.calcular_idade())