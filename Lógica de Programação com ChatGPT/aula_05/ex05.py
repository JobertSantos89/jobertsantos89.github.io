# Ex05. Faça um programa que peça 3 notas (utilizando o for) e mostre a média aritmética das notas

soma = 0
qtd_notas = int(input('Quantas notas deseja calcular a média? '))

for i in range(qtd_notas):
    nota = float(input(f'Digite a {i + 1}ª nota: '))
    soma += nota

media = soma / qtd_notas

print(f'A média das notas é: {media:.2f}')
