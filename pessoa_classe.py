class Pessoa: 
    def __init__(self, nome, idade ):
        self.nome = nome
        self. idade = idade

    def apresentar(self):
        print(f"O meu nome é {self.nome} e eu tenho {self.idade} anos!")

apresentacao_pessoa = Pessoa ("Julia", "20")
apresentacao_pessoa.apresentar()