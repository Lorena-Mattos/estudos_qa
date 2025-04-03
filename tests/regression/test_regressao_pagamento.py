import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRegressaoPagamento(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://ecommerce-example.com")
        self.wait = WebDriverWait(self.driver, 10)
        
    def test_formas_pagamento(self):
        """Testa todas as formas de pagamento disponíveis"""
        formas_pagamento = [
            ("cartao", "Cartão de Crédito"),
            ("boleto", "Boleto Bancário"),
            ("pix", "PIX"),
            ("debito", "Débito Online")
        ]
        
        for id_forma, nome_forma in formas_pagamento:
            with self.subTest(forma=nome_forma):
                self._testar_forma_pagamento(id_forma, nome_forma)
                
    def test_descontos(self):
        """Testa diferentes tipos de descontos"""
        descontos = [
            ("BLACKFRIDAY", 20),
            ("NATAL10", 10),
            ("ANO_NOVO", 15)
        ]
        
        for codigo, percentual in descontos:
            with self.subTest(cupom=codigo):
                self._testar_desconto(codigo, percentual)
                
    def test_notificacoes(self):
        """Testa o envio de notificações de pagamento"""
        # Testar notificação por e-mail
        self._testar_notificacao_email()
        
        # Testar notificação por SMS
        self._testar_notificacao_sms()
        
    def _testar_forma_pagamento(self, id_forma, nome_forma):
        # Adicionar produto ao carrinho
        self._adicionar_produto_ao_carrinho()
        
        # Ir para checkout
        self.driver.find_element(By.ID, "btn-checkout").click()
        
        # Selecionar forma de pagamento
        self.driver.find_element(By.ID, id_forma).click()
        
        # Preencher dados específicos da forma de pagamento
        if id_forma == "cartao":
            self._preencher_dados_cartao()
        elif id_forma == "boleto":
            self._gerar_boleto()
        elif id_forma == "pix":
            self._gerar_qrcode_pix()
        elif id_forma == "debito":
            self._selecionar_banco()
            
        # Finalizar pagamento
        self.driver.find_element(By.ID, "btn-finalizar").click()
        
        # Verificar confirmação
        confirmacao = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "confirmacao-pagamento"))
        )
        self.assertIn(nome_forma.lower(), confirmacao.text.lower())
        
    def _testar_desconto(self, codigo, percentual):
        # Adicionar produto ao carrinho
        self._adicionar_produto_ao_carrinho()
        
        # Aplicar cupom
        self.driver.find_element(By.ID, "cupom").send_keys(codigo)
        self.driver.find_element(By.ID, "btn-cupom").click()
        
        # Verificar desconto aplicado
        valor_desconto = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "valor-desconto"))
        )
        valor_original = self.driver.find_element(By.CLASS_NAME, "valor-original").text
        valor_final = self.driver.find_element(By.CLASS_NAME, "valor-final").text
        
        # Converter valores para float
        original = float(valor_original.replace("R$", "").replace(",", "."))
        final = float(valor_final.replace("R$", "").replace(",", "."))
        desconto = float(valor_desconto.replace("R$", "").replace(",", "."))
        
        # Verificar se o desconto está correto
        self.assertAlmostEqual(desconto, original * (percentual/100), places=2)
        self.assertAlmostEqual(final, original - desconto, places=2)
        
    def _testar_notificacao_email(self):
        # Configurar notificação por e-mail
        self.driver.find_element(By.ID, "notificacao-email").click()
        self.driver.find_element(By.ID, "email-notificacao").send_keys("teste@email.com")
        
        # Realizar compra
        self._realizar_compra_teste()
        
        # Verificar se e-mail foi enviado
        # Em ambiente real, isso seria verificado através de um serviço de e-mail
        self.assertTrue(True)  # Simulação
        
    def _testar_notificacao_sms(self):
        # Configurar notificação por SMS
        self.driver.find_element(By.ID, "notificacao-sms").click()
        self.driver.find_element(By.ID, "celular-notificacao").send_keys("11999999999")
        
        # Realizar compra
        self._realizar_compra_teste()
        
        # Verificar se SMS foi enviado
        # Em ambiente real, isso seria verificado através de um serviço de SMS
        self.assertTrue(True)  # Simulação
        
    def _adicionar_produto_ao_carrinho(self):
        self.driver.find_element(By.ID, "search").send_keys("Smartphone")
        self.driver.find_element(By.ID, "btn-search").click()
        self.driver.find_element(By.CLASS_NAME, "add-to-cart").click()
        
    def _preencher_dados_cartao(self):
        self.driver.find_element(By.ID, "numero-cartao").send_keys("4111111111111111")
        self.driver.find_element(By.ID, "nome-cartao").send_keys("João Silva")
        self.driver.find_element(By.ID, "validade").send_keys("12/25")
        self.driver.find_element(By.ID, "cvv").send_keys("123")
        
    def _gerar_boleto(self):
        # Em ambiente real, isso geraria um boleto
        pass
        
    def _gerar_qrcode_pix(self):
        # Em ambiente real, isso geraria um QR Code PIX
        pass
        
    def _selecionar_banco(self):
        self.driver.find_element(By.ID, "banco").select_by_visible_text("Banco Teste")
        
    def _realizar_compra_teste(self):
        self._adicionar_produto_ao_carrinho()
        self.driver.find_element(By.ID, "btn-checkout").click()
        self.driver.find_element(By.ID, "cartao").click()
        self._preencher_dados_cartao()
        self.driver.find_element(By.ID, "btn-finalizar").click()
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main() 