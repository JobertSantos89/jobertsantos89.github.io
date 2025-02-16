class Endereco:
    def __init__(self, cep: str, rua: str, bairro: str, numero: str, cidade: str, estado: str):
        self.cep = cep
        self.rua = rua
        self.bairro = bairro
        self.numero = numero
        self.cidade = cidade
        self.estado = estado

    def formatar(self) -> str:
        return f'{self.rua}, {self.numero} - {self.bairro} | {self.cidade} - {self.estado}, {self.cep}'
    
    def __str__(self):
        return self.formatar()


class Pessoa:
    def __init__(self, nome: str, idade: int, endereco: Endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco


endereco = Endereco('12333-123', 'Rua Tal', 'Logo Ali', '123', 'Rio Branco', 'AC')
pessoa = Pessoa('Dinossauro', 200, endereco)

print(pessoa.endereco.formatar())