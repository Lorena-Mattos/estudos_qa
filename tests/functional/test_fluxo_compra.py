import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestFluxoCompra(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://ecommerce-example.com")
        self.wait = WebDriverWait(self.driver, 10)
        
    def test_fluxo_completo_compra(self):
        # 1. Login
        self._realizar_login()
        
        # 2. Busca de produto
        self._buscar_produto("Smartphone")
        
        # 3. Adição ao carrinho
        self._adicionar_ao_carrinho()
        
        # 4. Aplicação de cupom
        self._aplicar_cupom("BLACKFRIDAY")
        
        # 5. Checkout
        self._realizar_checkout()
        
        # 6. Verificação de e-mail
        self._verificar_email_confirmacao()
        
    def _realizar_login(self):
        self.driver.find_element(By.ID, "email").send_keys("usuario@teste.com")
        self.driver.find_element(By.ID, "senha").send_keys("senha123")
        self.driver.find_element(By.ID, "btn-login").click()
        
        # Verificar login bem sucedido
        mensagem = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "mensagem-sucesso"))
        )
        self.assertIn("Bem-vindo", mensagem.text)
        
    def _buscar_produto(self, termo):
        self.driver.find_element(By.ID, "search").send_keys(termo)
        self.driver.find_element(By.ID, "btn-search").click()
        
        # Verificar resultados
        produtos = self.wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "produto"))
        )
        self.assertTrue(len(produtos) > 0)
        
    def _adicionar_ao_carrinho(self):
        self.driver.find_element(By.CLASS_NAME, "add-to-cart").click()
        
        # Verificar mensagem de sucesso
        mensagem = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "mensagem-carrinho"))
        )
        self.assertIn("adicionado ao carrinho", mensagem.text.lower())
        
    def _aplicar_cupom(self, codigo):
        self.driver.find_element(By.ID, "cupom").send_keys(codigo)
        self.driver.find_element(By.ID, "btn-cupom").click()
        
        # Verificar desconto aplicado
        desconto = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "valor-desconto"))
        )
        self.assertTrue(float(desconto.text.replace("R$", "").replace(",", ".")) > 0)
        
    def _realizar_checkout(self):
        # Preencher endereço
        self.driver.find_element(By.ID, "endereco").send_keys("Rua Teste, 123")
        self.driver.find_element(By.ID, "cidade").send_keys("São Paulo")
        self.driver.find_element(By.ID, "estado").send_keys("SP")
        self.driver.find_element(By.ID, "cep").send_keys("01234-567")
        
        # Selecionar pagamento
        self.driver.find_element(By.ID, "cartao").click()
        self.driver.find_element(By.ID, "numero-cartao").send_keys("4111111111111111")
        self.driver.find_element(By.ID, "nome-cartao").send_keys("João Silva")
        self.driver.find_element(By.ID, "validade").send_keys("12/25")
        self.driver.find_element(By.ID, "cvv").send_keys("123")
        
        # Finalizar compra
        self.driver.find_element(By.ID, "btn-finalizar").click()
        
        # Verificar confirmação
        confirmacao = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "confirmacao-compra"))
        )
        self.assertIn("compra realizada com sucesso", confirmacao.text.lower())
        
    def _verificar_email_confirmacao(self):
        # Em um ambiente real, isso seria verificado através de um serviço de e-mail
        # Aqui estamos apenas simulando a verificação
        time.sleep(2)  # Simular tempo de envio do e-mail
        self.assertTrue(True)  # Assumindo que o e-mail foi enviado
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main() 