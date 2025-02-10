from datetime import date

class Cachorro:
    def __init__(self, nome: str, raca: str, data_nascimento: date):
        self.nome = nome
        self.raca = raca

        # Associacao
        self.data_nascimento = data_nascimento

    def latir(self):
        return f'{self.nome} está latindo... AU AU'

    def calcular_idade(self):
        hoje = date.today()
        idade = hoje.year - self.data_nascimento.year

        aniversario_nao_ocorreu_este_ano = (
            self.data_nascimento.month > hoje.month 
            and self.data_nascimento.day > hoje.day
        )
        if aniversario_nao_ocorreu_este_ano:
            idade -= 1

        return idade


    def __str__(self):
        return f"Cachorro(nome='{self.nome}', raca='{self.raca}', data_nascimento={self.data_nascimento})"


dog1 = Cachorro('Xena', 'Pitbull', date(2008, 2, 12))

print(dog1)
print(dog1.latir())
print(f'Idade da {dog1.nome}: {dog1.calcular_idade()}')