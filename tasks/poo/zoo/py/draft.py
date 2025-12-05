from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome: str):
        self.nome = nome

    def apresentar_nome(self):
        print(f"Eu sou um(a) {self.nome}!")

    @abstractmethod
    def fazer_som(self):
        pass
    @abstractmethod
    def mover(self):
        pass

class Leao(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def fazer_som(self):
        print("Rooaar!")
    def mover(self):
        print("O leao esta caminhando")

class Elefante(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def fazer_som(self):
        print("fruuu!")
    def mover(self):
        print("O elefante esta andando")

class Cobra(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)
    
    def fazer_som(self):
        print("ssssss!")
    def mover(self):
        print("A cobra esta rastejando")

def apresentar(animal: Animal):
    animal.apresentar_nome()
    animal.fazer_som()
    animal.mover()

    print(f"Tipo do objeto: {type(animal).__name__}")
    print("-" * 40)

leao = Leao("simba")
elefante = Elefante("dumbu")
cobra = Cobra("sucuri")

apresentar(leao)
apresentar(elefante)
apresentar(cobra)




        

    
