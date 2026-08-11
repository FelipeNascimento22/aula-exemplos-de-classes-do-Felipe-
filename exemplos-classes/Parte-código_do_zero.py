class Produto:

    def __init__(self, nome: str, preco: float, estoque: int):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def reduzir_estoque(self, quantidade: int) -> bool:
        #Reduz a quantidade em estoque se houver disponibilidade suficiente.
        if quantidade <= self.estoque:
            self.estoque -= quantidade
            return True
        else:
            print(
                f"Erro: Estoque insuficiente de '{self.nome}'. Restantes: {self.estoque} unidades."
            )
            return False


class CarrinhoDeCompras:

    def __init__(self):
        self.produtos = []

    def adicionar_ao_carrinho(self, produto: Produto, quantidade: int):
        #Adiciona uma tupla (produto, quantidade) ao carrinho caso o estoque seja reduzido com sucesso.
        if produto.reduzir_estoque(quantidade):
            self.produtos.append((produto, quantidade))
            print(
                f"Sucesso: {quantidade}x '{produto.nome}' adicionado(s) ao carrinho."
            )

    def mostrar_carrinho(self):
        #Percorre e exibe todos os itens salvos no carrinho e calcula o valor total.
        if not self.produtos:
            print("\nO carrinho está vazio.")
            return

        print("\n--- ITENS NO CARRINHO ---")
        total_compra = 0.0

        for produto, quantidade in self.produtos:
            subtotal = produto.preco * quantidade
            total_compra += subtotal
            print(
                f"• {produto.nome} | Qtd: {quantidade} | Unitário: R$ {produto.preco:.2f} | Subtotal: R$ {subtotal:.2f}"
            )

        print("-" * 25)
        print(f"TOTAL A PAGAR: R$ {total_compra:.2f}\n")


# Exemplo de uso do sistema:

# Instanciando produtos
p1 = Produto("Notebook", 3500.00, 5)
p2 = Produto("Mouse Sem Fio", 80.00, 10)
p3 = Produto("Teclado Mecânico", 250.00, 2)

# Instanciando o carrinho
carrinho = CarrinhoDeCompras()

# Adicionando itens ao carrinho
carrinho.adicionar_ao_carrinho(p1, 1)
carrinho.adicionar_ao_carrinho(p2, 2)

# Tentativa de compra acima do estoque disponível
carrinho.adicionar_ao_carrinho(p3, 5)

# Exibindo o estado do carrinho
carrinho.mostrar_carrinho()

# Verificando a atualização do estoque dos produtos
print(f"Estoque restante de {p1.nome}: {p1.estoque}")
print(f"Estoque restante de {p2.nome}: {p2.estoque}")
print(f"Estoque restante de {p3.nome}: {p3.estoque}")