# Ex03. Faça um programa para o calculo de juros, 
# peça o valor inicial, taxa de juros em porcentagem 
# (sem o % e considere que a taxa é ao mês) e quantidade 
# de tempo em meses. Ao final mostre o valor total
# - Formula: total_juros = valor_inicial * taxa * tempo 

# Entrada
print('--- Seu Investimento ---')
valor_inicial = float(input('Digite o valor inicial da aplicação: '))
taxa_juros = float(input('Digite a taxa de juros (%): '))
meses = int(input('Digite quantos meses deseja aplicar: '))

# Processamento
total_juros = valor_inicial * (taxa_juros / 100) * meses
valor_total = valor_inicial + total_juros

# Saida
print(f'Seu investimento rendeu R${total_juros:.2f} e você receberá R${valor_total:.2f}')