class Animal:
    def __init__(self, nome : str, barulho : str, idade : int = 0):
        self.nome = nome
        self.barulho = barulho
        self.idade = idade
    
    def fazer_barulho(self):
        print(f"{self.nome} fez {self.barulho}")

    def aniversario(self):
        self.idade += 1
        print(f"O {self.nome} fez {self.idade} anos!")

def main():
    cachorro = Animal("Pastor Alemão", "AU AU!", 2)
    vaca = Animal("Vaca", "MUUUU!", 1)
    tucano = Animal("Tucano", "Craa Craa!", 3)

    # Isto é polimorfismo, ambos os objetos são do tipo Animal, 
    # mas cada um tem seu próprio comportamento, ou seja, 
    # cada um faz barulho diferente
    cachorro.fazer_barulho()
    vaca.fazer_barulho()
    tucano.fazer_barulho()

    cachorro.aniversario()
    vaca.aniversario()
    tucano.aniversario()

    cachorro.fazer_barulho()
    vaca.fazer_barulho()
    tucano.fazer_barulho()
    
    cachorro.aniversario()
    vaca.aniversario()
    tucano.aniversario()
    # Os dois objetos são animais, mas o que os diferenciam são seus nomes e barulhos, 
    # como os dois objetos foram iniciados pela mesma classe, 
    # ambos têm acesso aos mesmos métodos

if __name__ == "__main__":
    main()