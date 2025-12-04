class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def exibir_info(self):
        print(f"Produto: {self.nome}, Preço: {self.preco}, Quantidade: {self.quantidade}")

    def calcular_total(self):
        return self.preco * self.quantidade


# Testando a classe
p1 = Produto("Camisa", 50, 3)

p1.exibir_info()
print("Total em estoque:", p1.calcular_total())



