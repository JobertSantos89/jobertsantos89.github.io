def calcular_media(nota1: float, nota2: float, nota3: float) -> float:
    media = (nota1 + nota2 + nota3) / 3
    return media

n1 = float(input('Digite a 1ª nota: '))
n2 = float(input('Digite a 2ª nota: '))
n3 = float(input('Digite a 3ª nota: '))

media = calcular_media(n1, n2, n3)

print(f'A média do aluno é {media:.2f}')