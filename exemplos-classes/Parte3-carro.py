import time
class Carro:
    def __init__(self, modelo : str, marca : str, quilometragem: int = 0):
        self.modelo = modelo
        self.marca = marca
        self.combustivel = 100
        self.quilometragem = quilometragem
        
    def painel(self):
        print(f"Painel do Carro\n\nSeu carro o {self.modelo}.\nÉ da marca {self.marca}.\nTem {self.combustivel} de combustivel.")
        time.sleep(4)
    def fazer_barulho(self):
        if self.combustivel - 2 >= 0:
           self.combustivel -= 2
           print(f"{self.modelo} está fazendo barulho! \nCombustível: {self.combustivel}")
        else:
           print("Sem combustível para isso!")
    
    def acelerar(self):
        if self.combustivel - 10 >= 0:
           self.combustivel -= 10
           self.quilometragem += 15
           print(f"{self.modelo} acelerou! \nCombustível: {self.combustivel}| Quilometragem: {self.quilometragem} km")
           time.sleep(1)
        else:
           print("Sem combustível para isso!")

    def abastecer(self):
        self.quilometragem = 0
        num1 = 0
        self.resposta = int(input("Você percebe que o carro esta com pouca gasolina, deseja abastecer?\n1- sim, quero abastecer.\n2- não, eu não entendo de carros."))
        match self.resposta:
            case 1:
                self.resposta1 = int(input("O frentista é seu amigo então 1L é R$1. Quanto vc quer abastecer?(100): "))
                num1 += self.resposta1
                if num1 <= 100:
                    self.combustivel += num1
                else:
                    print("vc coloca gasolina demais e esvazia.")
            case 2:
                print("mds... vai acabar a gasolina!")




def main():
    onyx = Carro("Onyx", "Chevrolet")
    onyx.painel()
    while onyx.combustivel > 0:
        onyx.acelerar()
        onyx.acelerar()
        onyx.acelerar()
        onyx.acelerar()
        onyx.acelerar()
        onyx.acelerar()
        onyx.acelerar()
        onyx.acelerar()
        onyx.acelerar()
        onyx.acelerar()
        onyx.abastecer()
        onyx.acelerar()

if __name__ == "__main__":
    main()