# Qual é a saída do seguinte código?

class Pessoa: 

    def __init__(self, nome, idade): 

        self.__nome = nome 

        self.__idade = idade 

    def get_nome(self): 

        return self.__nome 



pessoa = Pessoa("Maria", 30) 

print(pessoa.get_nome()) 


# a) Maria


# b) 30


# c) Erro


# d) None


# e) pessoa

# f