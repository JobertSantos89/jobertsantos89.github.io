def maior_numero(n1, n2, n3):
    # Verifica se n1 é maior que n2 e n3
    if n1 > n2 and n1 > n3:
        return n1
    # Verifica se n2 é maior que n1 e n3
    elif n2 > n1 and n2 > n3:
        return n2
    # Caso o número 3 seja o maior
    else:
        return n3

numero_maior = maior_numero(30, 40, 150)
print("O maior número é:", numero_maior)