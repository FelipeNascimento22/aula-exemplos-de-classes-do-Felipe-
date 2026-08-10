from datetime import datetime, timedelta

class ContaBancaria:
    def __init__(self, titular : str):
        self.titular = titular
        self.saldo = 0
        self.extrato = []
    
    def mostrar_informações(self):
        print(f"{self.titular}\nSaldo Atual: {self.saldo}")
    
    def mostrar_extrato(self):
        for i in self.extrato:
            print(f"{i["data"]} > {i["movimento"]}")
        print("\n")

    def atualizar_extrato(self, transacao : float):
        
        self.extrato.append({"data": datetime.now(),"movimento": transacao})
    
    def adicionar_saldo(self, valor):
        self.saldo += valor
        self.atualizar_extrato(valor)
    
    def fazer_pix(self, valor):
        if self.saldo - valor < 0:
            print("Saldo insuficiente!")
        else:
            self.saldo -= valor
            self.atualizar_extrato(-valor)

minha_conta = ContaBancaria("Gabriel")
minha_conta.adicionar_saldo(1000)
minha_conta.mostrar_extrato()
minha_conta.fazer_pix(400.2)
minha_conta.mostrar_extrato()

minha_conta.mostrar_informações()
