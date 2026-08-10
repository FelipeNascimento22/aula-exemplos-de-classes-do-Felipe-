class ClasseMae:
    def __init__(self):
        self.nome = 'Classe Mãe'
        self.valor = 10
        self.ativo = True
    
    def metodo1(self):
        return 'Metodo 1 da classe mae'

class ClasseFilha(ClasseMae):
    def __init__(self):
        super().__init__()
        self.nome = 'Classe Filha'
    # O atributo super() é usado para chamar o método da classe mãe, 
    # permitindo que a classe filha herde o comportamento da classe mãe e, 
    # ao mesmo tempo, possa sobrescrever ou estender esse comportamento.
    
    def metodo2(self):
        return 'Metodo 2 da classe filha'

minha_classe_filha = ClasseFilha()
print(minha_classe_filha.nome)       # Saída: Classe Filha
print(minha_classe_filha.valor)      # Saída: 10
print(minha_classe_filha.metodo1())  # Saída: Metodo 1 da classe mae
print(minha_classe_filha.metodo2())  # Saída: Metodo 2 da classe filha