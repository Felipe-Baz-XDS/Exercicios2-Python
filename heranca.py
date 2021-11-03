class Animal:
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca
    
    def caminha(self):
        print(f"{self.nome} esta caminhando!")
    
    def __str__(self):
        return f"Nome: {animal.nome} - Raça: {animal.raca}"


class Cachorro(Animal):
    def __init__(self, nome, raca):
            super().__init__(nome, raca)

    def late(self):
        print(f"{self.nome} esta latindo!")


class Gato(Animal):
    def __init__(self, nome, raca):
            super().__init__(nome, raca)

    def mia(self):
        print(f"{self.nome} esta miando!")

def fazerCarinho(animal):
    print(f"{animal.nome} esta recebendo carinho!")

if __name__ == "__main__":
    gato = Gato("Mia", "gatinho preto")
    dog = Cachorro("thor", "Golden")

    dog.caminha()
    dog.late()
    print("\n")
    gato.caminha()
    gato.mia()
    print("\n")
    petshop = [gato, dog]
    for animal in petshop:
        print(animal)
        fazerCarinho(animal)
        print("\n")
    