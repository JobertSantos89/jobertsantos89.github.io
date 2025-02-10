# Paradigma Procedural
from datetime import date

nome = 'Lucas'
altura = 1.78
data_nascimento = date(1997, 12, 18)

idade = (date.today() - data_nascimento).days // 365


# Paradigma Funcional
pessoa1 = {
    'nome': 'Lucas',
    'altura': 1.78,
    'data_nascimento': date(1997, 12, 18)
}

pessoa2 = {
    'nome': 'Davi',
    'altura': 1.72,
    'data_nascimento': date(2004, 1, 14)
}

def calcular_idade(pessoa: dict) -> int:
    return (date.today() - pessoa.get('data_nascimento')).days // 365

print(calcular_idade(pessoa1))
print(calcular_idade(pessoa2))