# Passo 1: Solicitar o Salário Mensal
salario_mensal = float(input("Digite quanto você ganha por mês: "))

# Passo 2: Solicitar o Número de Horas Trabalhadas na Semana
horas_semanais = float(input("Digite o número de horas trabalhadas na semana: "))

# Passo 3: Calcular o Total de Horas Trabalhadas no Mês (considerando 4 semanas)
horas_mensais = horas_semanais * 4

# Passo 4: Calcular o Salário por Hora
salario_por_hora = salario_mensal / horas_mensais

# Passo 5: Mostrar o Salário por Hora Calculado para o Usuário
print(f"O seu salário por hora é: R${salario_por_hora: .2f}")
