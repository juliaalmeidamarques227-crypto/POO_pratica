class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def ligar(self):
        print(f"O {self.marca} {self.modelo} está ligando!")

meu_carro = Carro("Fiat", "Argo")
meu_carro.ligar("O meu {}")

