class Aluno:
    GABARITOS = [
    ["a", "b", "a", "d", "c"], 
    ["c", "b", "d", "c", "a"], 
    ["b", "b", "b", "b", "b"]
]
                
    

    def __init__(self, nome: str, sobrenome: str, idade: int):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.hist_notas = []
        self.media = 0
        self.situacao = "Em andamento"


    def fazer_prova(self, respostas: tuple[str, ...]):
        self.nota = 0
        for i in range(0,2):
            gabarito_da_vez = self.GABARITOS[i]
            for resposta, correta in zip(respostas, gabarito_da_vez):
                if resposta == correta:
                    self.nota += 2
            self.hist_notas.append(self.nota)

    def ver_nota(self):
        print(f"Aluno(a): {self.nome} {self.sobrenome} | e sua média é: {self.media}/10 | e você está: {self.situacao}")

    def calcular_media(self):
        self.media = sum(self.hist_notas) / len(self.hist_notas)

    def boletim(self):
        if self.media >=7:
            self.situacao = "Aprovado!"
        else:
            self.situacao = "Reprovado, betinha."
            
def main():
    arthur = Aluno("Arthur José", "Figueiredo", 18)
    
    arthur.fazer_prova(["a", "b", "a", "d", "d"])
    arthur.calcular_media()
    arthur.boletim()
    arthur.ver_nota()
if __name__ == "__main__":
    main()