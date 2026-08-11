from datetime import datetime, timedelta
import time 

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
        if self.saldo < -500:
            print("Saldo insuficiente! ja está no negativo!")
        else:
            self.saldo -= valor
            self.atualizar_extrato(-valor)
            if self.saldo < -500:
                print("Saldo insuficiente! ja está no negativo!")
                self.saldo += valor
            else:
                print("Pix feito com suceso!")
        return self.saldo

    def transferir(self, conta_destino):
        valor = minha_conta.fazer_pix(int(input("Quanto vc deseja transferir?: ")))
        self.saldo -= valor
        conta_destino.adicionar_saldo(valor)
        
        
            
        
conta_destino = ContaBancaria("Felipe")
minha_conta = ContaBancaria("Gabriel")
minha_conta.adicionar_saldo(1500)
minha_conta.mostrar_extrato()
minha_conta.fazer_pix(909)
minha_conta.mostrar_extrato()

minha_conta.mostrar_informações()

minha_conta.transferir(conta_destino)
time.sleep(2)

print(conta_destino.saldo)