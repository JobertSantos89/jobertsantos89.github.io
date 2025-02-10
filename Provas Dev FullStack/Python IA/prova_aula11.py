class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print("Este animal faz um som.")

class Cachorro(Animal):
    def falar(self):
        print(f"{self.nome} diz: O cachorro late.")

class Gato(Animal):
    def falar(self):
        print(f"{self.nome} diz: O gato mia.")


dog = Cachorro("Rex")
cat = Gato("Mia")


dog.falar()  
cat.falar()  

