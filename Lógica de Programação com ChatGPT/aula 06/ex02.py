print('----------- Calculador de Juros Simples -------------')
capital = float(input('Quanto deseja aplicar? -> '))
taxa_juros = float(input('Qual é a taxa de juros percentual (mensal)? -> '))
meses = float(input('Quantos meses deseja deixar o valor aplicado? -> '))

total_juros = capital * (taxa_juros / 100) * meses
capital_final = capital + total_juros

print(f'O seu dinheiro irá render {total_juros} na taxa {taxa_juros}% ao mês durante {meses} meses')
print(f'Total a receber: {capital_final:.2f}')
