# Multiplos Valores

# Passando uma lista
def calcular_media(numeros: list[float]) -> float:
    return sum(numeros) / len(numeros)

minha_lista = [53, 65, 34, 7, 34]
media1 = calcular_media(minha_lista)
print(media1)

media2 = calcular_media([4, 5, 6, 7, 9, 4, 2, 4, 4])
print(media2)
