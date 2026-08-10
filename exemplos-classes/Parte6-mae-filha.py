class Animal:
    def __init__(self, nome, barulho):
        self.nome = nome
        self.barulho = barulho

    def fazer_barulho(self):
        print(f"{self.nome} faz {self.barulho}")

class Cachorro(Animal):
    def __init__(self, raca = None):
        super().__init__(nome = "Cachorro", barulho = "AU AU!")
        self.raca = raca

    def fazer_barulho(self):
        print(f"{self.nome} da raça {self.raca} faz {self.barulho}")
    
    def informacoes(self):
        print(f"Nome: {self.nome}, Barulho: {self.barulho}, Raça: {self.raca}")

pastor_alemao = Cachorro("Pastor Alemão")
pastor_alemao.fazer_barulho()