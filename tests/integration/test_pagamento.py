import unittest
from src.carrinho import CarrinhoDeCompras, Produto
from src.pagamento import SistemaDePagamento

class TestIntegracaoPagamento(unittest.TestCase):
    def setUp(self):
        self.carrinho = CarrinhoDeCompras()
        self.sistema_pagamento = SistemaDePagamento()
        self.produto = Produto("Smartphone", 1000.00)
        
    def test_processamento_pagamento_sucesso(self):
        # Adicionar produto ao carrinho
        self.carrinho.adicionar_item(self.produto)
        
        # Processar pagamento
        resultado = self.sistema_pagamento.processar_pagamento(
            carrinho=self.carrinho,
            numero_cartao="4111111111111111",
            nome_titular="João Silva",
            data_validade="12/25",
            cvv="123"
        )
        
        # Verificar resultados
        self.assertTrue(resultado.sucesso)
        self.assertEqual(resultado.valor, 1000.00)
        self.assertIsNotNone(resultado.codigo_transacao)
        
    def test_processamento_pagamento_falha_cartao_invalido(self):
        self.carrinho.adicionar_item(self.produto)
        
        resultado = self.sistema_pagamento.processar_pagamento(
            carrinho=self.carrinho,
            numero_cartao="1234567890123456",  # Cartão inválido
            nome_titular="João Silva",
            data_validade="12/25",
            cvv="123"
        )
        
        self.assertFalse(resultado.sucesso)
        self.assertEqual(resultado.mensagem_erro, "Cartão inválido")
        
    def test_processamento_pagamento_com_desconto(self):
        self.carrinho.adicionar_item(self.produto)
        self.carrinho.aplicar_desconto(10)  # 10% de desconto
        
        resultado = self.sistema_pagamento.processar_pagamento(
            carrinho=self.carrinho,
            numero_cartao="4111111111111111",
            nome_titular="João Silva",
            data_validade="12/25",
            cvv="123"
        )
        
        self.assertTrue(resultado.sucesso)
        self.assertEqual(resultado.valor, 900.00)  # 1000 - 10%

if __name__ == "__main__":
    unittest.main() 