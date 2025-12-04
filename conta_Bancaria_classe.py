class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print("Depósito realizado.")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print("Saque realizado.")
        else:
            print("Saldo insuficiente.")

    def extrato(self):
        print(f"Saldo atual: {self.saldo}")


# Criando uma conta
conta = ContaBancaria("Julia", 100)

# Testando métodos
conta.extrato()      # mostra o saldo
conta.depositar(50)  # adiciona 50
conta.extrato()      # mostra o novo saldo
conta.sacar(30)      # saca 30
conta.extrato()      # mostra o saldo depois do saque
conta.sacar(200)     # tentativa de saque maior que o saldo



