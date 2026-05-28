class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, nome, preco, quantidade=1):
        self.itens.append({
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade
        })

    def remover_item(self, nome):
        self.itens = [item for item in self.itens if item["nome"] != nome]

    def calcular_total(self):
        return sum(item["preco"] * item["quantidade"] for item in self.itens)

    def aplicar_desconto(self, percentual):
        if percentual > 20:
            raise ValueError("Desconto máximo permitido é de 20%")
        if percentual < 0:
            raise ValueError("Desconto não pode ser negativo")
        total = self.calcular_total()
        desconto = total * (percentual / 100)
        return total - desconto