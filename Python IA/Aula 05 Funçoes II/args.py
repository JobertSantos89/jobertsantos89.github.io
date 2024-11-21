# Args 
# Ao declarar um parametro com "*" você pode passar "N" 
# parametros e eles chegarão na função como uma tupla.
def somar(*args: float):
    total = 0
    for arg in args:
        total += arg

    return total

# Exemplos...
print(somar(2, 5, 6, 7))
print(somar(6, 8, 3, 9, 9, 3, 65))
