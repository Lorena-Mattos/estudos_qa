class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class CarrinhoDeCompras:
    def __init__(self):
        self.itens = []
        self.desconto = 0
        
    def adicionar_item(self, produto):
        self.itens.append(produto)
        
    def remover_item(self, produto):
        if produto in self.itens:
            self.itens.remove(produto)
            
    def calcular_total(self):
        total = sum(item.preco for item in self.itens)
        return total * (1 - self.desconto/100)
        
    def aplicar_desconto(self, percentual):
        self.desconto = percentual
        
    def limpar(self):
        self.itens = []
        self.desconto = 0 