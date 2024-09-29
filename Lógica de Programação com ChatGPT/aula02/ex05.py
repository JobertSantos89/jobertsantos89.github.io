# Ex05. Faça um programa que peça um numero, e informe se ele é positivo, negativo ou neutro (igual a zero)

numero = int(input('Digite um numero: '))

if numero > 0:
   print('O numero é positivo.')
elif numero < 0:
   print('O numero é negativo.')
else:
   print('O numero é neutro.')