import unittest
from src.carrinho import CarrinhoDeCompras, Produto

class TestCarrinhoDeCompras(unittest.TestCase):
    def setUp(self):
        self.carrinho = CarrinhoDeCompras()
        self.produto1 = Produto("Smartphone", 1000.00)
        self.produto2 = Produto("Capa", 50.00)
        
    def test_adicionar_produto(self):
        self.carrinho.adicionar_item(self.produto1)
        self.assertEqual(len(self.carrinho.itens), 1)
        self.assertEqual(self.carrinho.itens[0].nome, "Smartphone")
        
    def test_calcular_total(self):
        self.carrinho.adicionar_item(self.produto1)
        self.carrinho.adicionar_item(self.produto2)
        total = self.carrinho.calcular_total()
        self.assertEqual(total, 1050.00)
        
    def test_aplicar_desconto(self):
        self.carrinho.adicionar_item(self.produto1)
        self.carrinho.aplicar_desconto(10)  # 10% de desconto
        total = self.carrinho.calcular_total()
        self.assertEqual(total, 900.00)
        
    def test_remover_produto(self):
        self.carrinho.adicionar_item(self.produto1)
        self.carrinho.adicionar_item(self.produto2)
        self.carrinho.remover_item(self.produto1)
        self.assertEqual(len(self.carrinho.itens), 1)
        self.assertEqual(self.carrinho.itens[0].nome, "Capa")
        
    def test_limpar_carrinho(self):
        self.carrinho.adicionar_item(self.produto1)
        self.carrinho.adicionar_item(self.produto2)
        self.carrinho.limpar()
        self.assertEqual(len(self.carrinho.itens), 0)
        self.assertEqual(self.carrinho.calcular_total(), 0.00)

if __name__ == "__main__":
    unittest.main() 