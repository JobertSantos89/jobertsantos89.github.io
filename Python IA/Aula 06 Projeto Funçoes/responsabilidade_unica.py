# Principios SOLID
# S - Single Responsability Principle
# O principio da responsabilidade unica diz que uma função
# deve conter somente uma responsabilidade

# Uma boa forma de entender se esse principio está sendo seguido, 
# é tentar colocar no nome da função tudo que ela está fazendo.

# Exemplo 1 ("Errado")
def calcular_imc_e_mostrar_na_tela(peso, altura):
    imc = peso / altura ** 2
    print(imc)

# Exemplo 2 (Certo)
def calcular_imc(peso, altura):
    return peso / altura ** 2