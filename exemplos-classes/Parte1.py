
print("Classes do zero!")

# Classes são criadores de objetos, objetos são unidades de dados que combinam variáveis e funções.
# Em Python tudo é um objeto, variáveis, tipos de dados, funções e etc

# Como identificar um objeto:
# - Ele ocupa um endereço da memória ram
# - Ele possui um tipo, que define suas funcionalidades
# - Objetos possuem métodos e atributos

# Exemplo da utilização de um objeto

letras = "um texto"     # uma variável é uma etiqueta, está etiqueta está colada em um dado
# O tipo deste dado é um objeto, ou seja, ele possui métodos
# Por isso, como estamos guardando uma variável string, vamos possuir acesso aos métodos de string com está variável

# Agora podemos utilizar os métodos de string nesta variável, métodos como .upper, .capitalize, .lower, .title(), .strip() etc
print(letras)
letras = letras.upper()
print(letras)

# Definimos que tipos de dados são objetos
# Definimos que todo objeto herda os métodos que a classe deste objeto possui
# Classes são moldes para criação de objetos

# Para exemplificar, vamos criar um pseudocódigo demonstrando a classe string, veja:

# Uma classe (também chamada de função construtora) cria objetos, a função __init__ é responsável pela inicialização deste objeto, os
# parâmetros da função __init__ devem ser passados na hora de inicar um novo objeto
class TipoString:
    def __init__(self, valor : str): # Este __init__ é chamado automaticamente quando o objeto é criado, o : ao lado do parâmetro
        # valor, dita qual tipo de dado deve ser recebido pela função de inicialização, este : pode ser usado em qualquer função
        self.valor = valor  # A palavra self, define que o valor nesta variável é única do objeto criado neste instante

    def alta(self):
        print("Colocar todos as letras de uma string em caixa alta")

    def baixa(self):
        print("Colocar todos as letras de uma string em caixa baixa")

    def titulo(self):
        print("Colocar a primeira letra de uma string em caixa alta")

# Ao criar um novo objeto com está classe, as funções da classe se tornam métodos deste objeto
# para criar um novo objeto, criamos uma variável, recebendo a classe, junto dos parâmetros de inicialização, neste caso, o "valor"

nova_string = TipoString("Novo texto")
nova_string.alta()
nova_string.baixa()
nova_string.titulo()
