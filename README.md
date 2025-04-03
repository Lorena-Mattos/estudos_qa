
# Roadmap para QA (Quality Assurance) - Passo a Passo Prático

## ✨ 1. Fundamentos de QA

### ✅ O que é QA e por que é importante?
- QA (Quality Assurance) garante que software funciona corretamente antes de ser entregue.
- Previne erros e melhora a experiência do usuário.
- QA pode ser **manual** (testes feitos por pessoas) ou **automático** (testes feitos por código).

### ✅ Tipos de Testes
1. **Testes Manuais**: Feitos por um tester interagindo com o sistema.
2. **Testes Automatizados**: Feitos por scripts que verificam o sistema automaticamente.
3. **Testes de Unidade**: Testam partes pequenas do código separadamente.
4. **Testes de Integração**: Testam módulos diferentes funcionando juntos.
5. **Testes Funcionais**: Testam se o sistema atende aos requisitos.
6. **Testes de Regressão**: Garantem que mudanças não quebram funcionalidades antigas.
7. **Testes de Carga**: Verificam o desempenho do sistema com muitos usuários.
8. **Testes End-to-End (E2E)**: Testam um fluxo completo do usuário, desde o início até o fim.

### ✅ Ferramentas Essenciais
- **Selenium** (para automação web, você já conhece!)
- **Cypress** (para testes end-to-end mais modernos)
- **PyTest** (para executar testes automatizados)
- **Postman** (para testar APIs)
- **JMeter** (para testes de desempenho)
- **REST Assured** (para testes de API em Java)
- **CI/CD com GitHub Actions, Jenkins, GitLab CI** (para rodar testes automáticos)

## ✨ 2. Testes Manuais

### ✅ Exercício prático:
1. Escolha um site simples (exemplo: [https://www.google.com](https://www.google.com)).
2. Tente usar o site e encontrar possíveis problemas (botões quebrados, falhas de layout, etc.).
3. Registre os problemas em uma planilha com:
   - Passos para reproduzir o erro
   - O que deveria acontecer
   - O que realmente aconteceu

## ✨ 3. Testes Automatizados com Python e Selenium

### ✅ Instalando Selenium
```bash
pip install selenium
```

### ✅ Primeiro Teste Automatizado
```python
from selenium import webdriver
from selenium.webdriver.common.by import By

# Abrir o navegador
driver = webdriver.Chrome()
driver.get("https://www.google.com")

# Encontrar o campo de busca e digitar algo
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("QA Selenium")
search_box.submit()

# Fechar o navegador
driver.quit()
```

**Desafio:** Execute esse script e veja os resultados!

## ✨ 4. Testes End-to-End com Cypress

### ✅ Instalando Cypress
```bash
npm install cypress --save-dev
```

### ✅ Criando um Teste Cypress
```javascript
describe('Teste de Busca no Google', () => {
  it('Deve buscar algo no Google', () => {
    cy.visit('https://www.google.com');
    cy.get('input[name="q"]').type('QA Cypress{enter}');
    cy.contains('QA Cypress');
  });
});
```

**Rodando o teste:**
```bash
npx cypress open
```

## ✨ 5. Testes de API com Postman e Python

### ✅ Testando uma API Manualmente
1. Baixe e instale o **Postman**.
2. Teste uma API pública, como:
   - URL: `https://jsonplaceholder.typicode.com/posts/1`
   - Método: GET

### ✅ Testando API com Python (usando Requests)
```python
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.json())
```

**Desafio:** Teste outras rotas dessa API e veja os resultados.

## ✨ 6. Criando Casos de Teste

### ✅ Como escrever um caso de teste?
1. **ID do Caso**: CT-001
2. **Título**: Testar login com credenciais válidas
3. **Passos**:
   - Acessar `https://exemplo.com/login`
   - Digitar "usuario@example.com" no campo de e-mail
   - Digitar "senha123" no campo de senha
   - Clicar no botão "Entrar"
4. **Resultado esperado**: Login bem-sucedido.
5. **Resultado real**: ??? (Preencher ao testar)
6. **Status**: Aprovado/Reprovado

**Desafio:** Crie um caso de teste para testar o cadastro de usuário.

## ✨ 7. CI/CD para QA

### ✅ Rodando Testes Automaticamente com GitHub Actions
```yaml
name: Run Tests
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2
      - name: Install dependencies
        run: npm install
      - name: Run Cypress tests
        run: npx cypress run
```

## 🚀 Conclusão
Esse roadmap cobre os primeiros passos para você iniciar na área de QA, de forma prática e direta, incluindo testes E2E e Cypress. 

**O que fazer agora?**
- Siga os passos e execute os exemplos práticos.
- Resolva os desafios propostos.
- Me pergunte se tiver dúvidas!

💪 Bora praticar e se tornar um QA ninja!


