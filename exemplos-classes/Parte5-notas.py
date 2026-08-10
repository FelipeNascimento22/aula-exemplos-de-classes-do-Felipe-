class Aluno:
    GABARITO = ("a", "b", "a", "d", "c")

    def __init__(self, nome: str, sobrenome: str, idade: int):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.nota = 0

    def fazer_prova(self, respostas: tuple[str, ...]):
        self.nota = 0
        for resposta, correta in zip(respostas, self.GABARITO):
            if resposta == correta:
                self.nota += 2

    def ver_nota(self):
        print(f"Aluno(a): {self.nome} {self.sobrenome} | Nota: {self.nota}/10")

def main():
    arthur = Aluno("Arthur José", "Figueiredo", 18)
    
    arthur.fazer_prova(("a", "b", "a", "d", "d"))
    arthur.ver_nota()

if __name__ == "__main__":
    main()