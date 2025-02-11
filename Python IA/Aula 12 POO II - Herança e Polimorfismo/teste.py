class Animal: 

    def fazer_som(self): 

        return "Som de animal" 



class Cachorro(Animal): 

    def fazer_som(self): 

        return "Latido"



cachorro = Cachorro() 



print(cachorro.fazer_som())