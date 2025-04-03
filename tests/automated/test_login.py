from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://ecommerce-example.com")
        
    def test_login_sucesso(self):
        # Localizar elementos
        email_input = self.driver.find_element(By.ID, "email")
        senha_input = self.driver.find_element(By.ID, "senha")
        botao_login = self.driver.find_element(By.ID, "btn-login")
        
        # Preencher formulário
        email_input.send_keys("usuario@teste.com")
        senha_input.send_keys("senha123")
        botao_login.click()
        
        # Verificar se login foi bem sucedido
        wait = WebDriverWait(self.driver, 10)
        mensagem_sucesso = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "mensagem-sucesso"))
        )
        self.assertIn("Bem-vindo", mensagem_sucesso.text)
        
    def test_login_falha(self):
        # Teste com credenciais inválidas
        email_input = self.driver.find_element(By.ID, "email")
        senha_input = self.driver.find_element(By.ID, "senha")
        botao_login = self.driver.find_element(By.ID, "btn-login")
        
        email_input.send_keys("usuario@invalido.com")
        senha_input.send_keys("senhaerrada")
        botao_login.click()
        
        # Verificar mensagem de erro
        wait = WebDriverWait(self.driver, 10)
        mensagem_erro = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "mensagem-erro"))
        )
        self.assertIn("Credenciais inválidas", mensagem_erro.text)
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main() 