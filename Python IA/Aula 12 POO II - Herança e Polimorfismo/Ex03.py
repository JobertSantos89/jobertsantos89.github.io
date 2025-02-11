class Calculadora:
    """Classe que implementa um método somar com polimorfismo"""
    
    def somar(self, a, b):
        """Método polimórfico que soma números ou concatena strings"""
        if isinstance(a, int) and isinstance(b, int):
            return a + b  # Soma de inteiros
        elif isinstance(a, str) and isinstance(b, str):
            return a + " " + b  # Concatenação de strings com espaço
        else:
            raise TypeError("Os tipos devem ser ambos inteiros ou ambos strings.")

# Criando uma instância da calculadora
calc = Calculadora()

# Exemplos de uso
print(calc.somar(10, 20))
print(calc.somar("Hello", "World"))

# Tentativa de misturar tipos (gera erro)
# print(calc.somar(10, "World"))  # TypeError: Os tipos devem ser ambos inteiros ou ambos strings.
