# Estrturas de Repetição (While = Loop) 
numero = 0 # Variavel de Controle && Input do Usuário
maior = None

while numero != 999:
    numero = int(input('Digite um numero ([999] para parar): '))

    if numero == 999:
        continue

    if maior == None or numero > maior:
        maior = numero

print(f'O maior numero digitado foi: {maior}')
print('Fim do programa')

