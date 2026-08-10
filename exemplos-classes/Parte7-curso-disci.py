class Disciplina:
    def __init__(self, nome):
        self.nome = nome

class Curso:
    def __init__(self, nome):
        self.nome = nome
        self.grade_curricular = []  # Catálogo de matérias oferecidas

    def adicionar_disciplina(self, disciplina):
        self.grade_curricular.append(disciplina)

class RegistroBoletim:
    def __init__(self, disciplina):
        self.disciplina = disciplina
        self.nota = None

class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.curso = None
        self.boletim = []  # Matérias que o aluno ESCOLHEU cursar

    def matricular_em_curso(self, curso):
        self.curso = curso
        print(f"{self.nome} entrou no curso de {curso.nome}.")

    def matricular_em_disciplina(self, nome_disciplina):
        if not self.curso:
            print(f"Erro: {self.nome} precisa estar em um curso antes de puxar matérias!")
            return

        # 1. Checa se o curso oferece essa matéria
        disciplina_ofertada = None
        for disc in self.curso.grade_curricular:
            if disc.nome == nome_disciplina:
                disciplina_ofertada = disc
                break

        if not disciplina_ofertada:
            print(f"Erro: A matéria '{nome_disciplina}' não existe no curso de {self.curso.nome}.")
            return

        # 2. Checa se o aluno já não se matriculou nela
        for registro in self.boletim:
            if registro.disciplina.nome == nome_disciplina:
                print(f"Aviso: {self.nome} já está cursando {nome_disciplina}.")
                return

        # 3. Matricula o aluno manualmente na matéria
        self.boletim.append(RegistroBoletim(disciplina_ofertada))
        print(f"-> {self.nome} se matriculou em: {nome_disciplina}")

    def lancar_nota(self, nome_disciplina, nota):
        for registro in self.boletim:
            if registro.disciplina.nome == nome_disciplina:
                registro.nota = nota
                print(f"Nota {nota} lançada em {nome_disciplina} para {self.nome}.")
                return
        print(f"Erro: {self.nome} não está matriculado(a) em {nome_disciplina}.")

    def ver_relatorio(self):
        print(f"\n--- Relatório de {self.nome} ({self.curso.nome if self.curso else 'Sem Curso'}) ---")
        if not self.boletim:
            print("Nenhuma disciplina matriculada.")
        for registro in self.boletim:
            nota_tela = registro.nota if registro.nota is not None else "Sem nota"
            print(f"> {registro.disciplina.nome}: {nota_tela}")
        print()


# --- TESTANDO A MATRÍCULA MANUAL ---

# 1. Criando o Curso e suas opções
eng = Curso("Engenharia de Computação")
eng.adicionar_disciplina(Disciplina("Cálculo 1"))
eng.adicionar_disciplina(Disciplina("Física Básica"))
eng.adicionar_disciplina(Disciplina("Algoritmos"))

# 2. Criando o Aluno
carlos = Aluno("Carlos")
carlos.matricular_em_curso(eng)

# 3. Carlos escolhe manualmente APENAS 2 matérias das 3 disponíveis
carlos.matricular_em_disciplina("Cálculo 1")
carlos.matricular_em_disciplina("Algoritmos")

# Tentando puxar uma matéria que não existe no curso dele
carlos.matricular_em_disciplina("Direito Constitucional") 

# 4. Lançando notas e vendo relatório
carlos.lancar_nota("Cálculo 1", 8.0)
carlos.ver_relatorio()