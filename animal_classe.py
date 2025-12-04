# Classe base
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        print("O animal faz um som.")

# Classe filha Cachorro (herda de Animal)
class Cachorro(Animal):
    def fazer_som(self):
        print("Au au!")

# Classe filha Gato (herda de Animal)
class Gato(Animal):
    def fazer_som(self):
        print("Miau!")


animal_generico = Animal("Bicho")
animal_generico.fazer_som()

dog = Cachorro("Thor")
dog.fazer_som()

cat = Gato("Luna")
cat.fazer_som()
