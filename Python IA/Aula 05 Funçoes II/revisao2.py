# Revisão Funções 2

# Type Hints
def dividir(num1: float, num2: float) -> float:
    return num1 / num2

# Passagem de Parametros
# Posicional
# 10 -> num1
# 2 -> num2
valor1 = dividir(10, 2)

# Nomeada
# 10 -> num2
# 2 -> num1
valor2 = dividir(num2=10, num1=2)

# Valores Padrão
def subtrair(num1: float, num2: float, num3: float = 0) -> float:
    return num1 - num2 - num3

# Se num3 for passado, ele considera o que foi informado.
resultado1 = subtrair(10, 2, 4) 

# Se num3 não for passado, ele considera o valor padrão.
resultado2 = subtrair(10, 5)