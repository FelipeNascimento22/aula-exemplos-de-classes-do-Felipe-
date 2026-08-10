class Animal:
    def __init__(self, nome : str, barulho : str):
        self.nome = nome
        self.barulho = barulho
    
    def fazer_barulho(self):
        print(f"{self.nome} fez {self.barulho}")

def main():
    cachorro = Animal("Pastor Alemão", "AU AU!")
    vaca = Animal("Vaca", "MUUUU!")

    # Isto é polimorfismo, ambos os objetos são do tipo Animal, 
    # mas cada um tem seu próprio comportamento, ou seja, 
    # cada um faz barulho diferente
    cachorro.fazer_barulho()
    vaca.fazer_barulho()

    # Os dois objetos são animais, mas o que os diferenciam são seus nomes e barulhos, 
    # como os dois objetos foram iniciados pela mesma classe, 
    # ambos têm acesso aos mesmos métodos

if __name__ == "__main__":
    main()