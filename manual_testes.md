# Manual de Testes de Software
## Guia Completo para Iniciantes em QA

### Índice
1. [Introdução](#introdução)
2. [Configuração do Ambiente](#configuração-do-ambiente)
3. [Testes Manuais](#testes-manuais)
4. [Testes Automatizados](#testes-automatizados)
5. [Testes de Unidade](#testes-de-unidade)
6. [Testes de Integração](#testes-de-integração)
7. [Testes Funcionais](#testes-funcionais)
8. [Testes de Regressão](#testes-de-regressão)
9. [Testes de Carga](#testes-de-carga)
10. [Testes End-to-End](#testes-end-to-end)

## Introdução

Este manual foi criado para ajudar iniciantes na área de Qualidade de Software (QA) a entender e implementar diferentes tipos de testes. Vamos explorar cada tipo de teste através de exemplos práticos em um sistema de e-commerce.

## Configuração do Ambiente

### Pré-requisitos
- Python 3.8 ou superior
- Node.js 14 ou superior
- Navegador Chrome/Chromium
- Editor de código (VS Code recomendado)

### Instalação das Dependências

1. **Python e suas bibliotecas**
```bash
pip install selenium==4.30.0
pip install locust==2.33.2
pip install pytest==8.3.5
pip install pytest-selenium==4.1.0
pip install webdriver-manager==4.0.2
```

2. **Node.js e Cypress**
```bash
npm install cypress
```

## Testes Manuais

### O que são Testes Manuais?
Testes manuais são aqueles executados por um tester interagindo diretamente com o sistema, sem o uso de automação. São essenciais para validar a experiência do usuário e encontrar problemas que podem passar despercebidos em testes automatizados.

### Checklist de Testes Manuais
O arquivo `tests/manual/checklist_teste_manual.md` contém um checklist detalhado para testes manuais. Vamos analisar cada seção:

#### 1. Teste de Login
```markdown
### Cenário: Login com credenciais válidas
- [ ] Acessar a página de login
- [ ] Inserir e-mail válido: teste@email.com
- [ ] Inserir senha válida: 123456
```

**Explicação:**
- Cada item do checklist representa um passo a ser executado manualmente
- O símbolo `[ ]` indica que o passo precisa ser marcado quando concluído
- As credenciais são exemplos e devem ser substituídas por dados reais do sistema

#### 2. Teste de Busca de Produtos
```markdown
### Cenário: Busca com resultados
- [ ] Acessar a página inicial
- [ ] Inserir termo de busca: "Smartphone"
```

**Explicação:**
- Este cenário testa a funcionalidade de busca do sistema
- O termo "Smartphone" é um exemplo e pode ser substituído por outros produtos

### Como Executar Testes Manuais
1. Abra o checklist no editor de texto
2. Siga cada passo sequencialmente
3. Marque os itens conforme forem concluídos
4. Documente qualquer problema encontrado
5. Tire screenshots quando necessário

## Testes Automatizados

### O que são Testes Automatizados?
Testes automatizados são executados por scripts que simulam a interação do usuário com o sistema. Eles são mais rápidos e podem ser executados repetidamente.

### Exemplo: Teste de Login Automatizado
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://ecommerce-example.com")
```

**Explicação:**
- `selenium`: Biblioteca para automação de navegadores
- `webdriver`: Classe que controla o navegador
- `unittest`: Framework para testes em Python
- `setUp`: Método executado antes de cada teste

### Componentes do Teste Automatizado
1. **Configuração do Navegador**
```python
self.driver = webdriver.Chrome()
```
- Cria uma nova instância do Chrome
- Pode ser substituído por outros navegadores (Firefox, Edge)

2. **Localização de Elementos**
```python
email_input = self.driver.find_element(By.ID, "email")
```
- `find_element`: Encontra um elemento na página
- `By.ID`: Localiza o elemento pelo atributo ID
- Outros métodos de localização: `By.CLASS_NAME`, `By.XPATH`, etc.

3. **Interação com Elementos**
```python
email_input.send_keys("usuario@teste.com")
```
- `send_keys`: Simula digitação no campo
- Outros métodos: `click()`, `clear()`, `submit()`

## Testes de Unidade

### O que são Testes de Unidade?
Testes que verificam partes pequenas e isoladas do código, como funções ou classes individuais.

### Exemplo: Teste da Classe CarrinhoDeCompras
```python
class TestCarrinhoDeCompras(unittest.TestCase):
    def setUp(self):
        self.carrinho = CarrinhoDeCompras()
        self.produto1 = Produto("Smartphone", 1000.00)
```

**Explicação:**
- `setUp`: Prepara o ambiente para cada teste
- Cria instâncias necessárias para os testes

### Testando Métodos da Classe
```python
def test_adicionar_produto(self):
    self.carrinho.adicionar_item(self.produto1)
    self.assertEqual(len(self.carrinho.itens), 1)
```

**Explicação:**
- `test_adicionar_produto`: Nome do teste
- `adicionar_item`: Método sendo testado
- `assertEqual`: Verifica se o resultado é igual ao esperado

## Testes de Integração

### O que são Testes de Integração?
Testes que verificam a interação entre diferentes partes do sistema.

### Exemplo: Teste de Integração entre Carrinho e Pagamento
```python
def test_processamento_pagamento_sucesso(self):
    self.carrinho.adicionar_item(self.produto)
    resultado = self.sistema_pagamento.processar_pagamento(
        carrinho=self.carrinho,
        numero_cartao="4111111111111111"
    )
```

**Explicação:**
- Testa a integração entre duas classes: `CarrinhoDeCompras` e `SistemaDePagamento`
- Verifica se o processamento do pagamento funciona corretamente

## Testes Funcionais

### O que são Testes Funcionais?
Testes que verificam se o sistema atende aos requisitos funcionais.

### Exemplo: Teste do Fluxo de Compra
```python
def test_fluxo_completo_compra(self):
    # 1. Login
    self._realizar_login()
    # 2. Busca de produto
    self._buscar_produto("Smartphone")
    # 3. Adição ao carrinho
    self._adicionar_ao_carrinho()
```

**Explicação:**
- Testa um fluxo completo do usuário
- Cada método testa uma parte específica do fluxo
- Os métodos são organizados em ordem lógica

## Testes de Regressão

### O que são Testes de Regressão?
Testes que garantem que novas alterações não quebrem funcionalidades existentes.

### Exemplo: Teste de Regressão do Sistema de Pagamento
```python
def test_formas_pagamento(self):
    formas_pagamento = [
        ("cartao", "Cartão de Crédito"),
        ("boleto", "Boleto Bancário"),
        ("pix", "PIX")
    ]
    
    for id_forma, nome_forma in formas_pagamento:
        self._testar_forma_pagamento(id_forma, nome_forma)
```

**Explicação:**
- Testa todas as formas de pagamento disponíveis
- Usa `subTest` para testar cada forma separadamente
- Facilita a identificação de qual forma de pagamento falhou

## Testes de Carga

### O que são Testes de Carga?
Testes que verificam o desempenho do sistema sob carga de usuários.

### Exemplo: Teste de Carga com Locust
```python
from locust import HttpUser, task, between

class UsuarioEcommerce(HttpUser):
    wait_time = between(1, 3)
    
    @task(3)
    def ver_produtos(self):
        self.client.get("/produtos")
```

**Explicação:**
- `HttpUser`: Classe base para usuários simulados
- `wait_time`: Tempo de espera entre requisições
- `@task`: Define uma tarefa que o usuário pode executar
- O número (3) indica a frequência relativa da tarefa

## Testes End-to-End

### O que são Testes End-to-End?
Testes que verificam o fluxo completo do sistema, do início ao fim.

### Exemplo: Teste E2E com Cypress
```javascript
describe('Fluxo de Compra E2E', () => {
    it('Deve completar uma compra com sucesso', () => {
        cy.visit('/')
        cy.get('[data-test="login-button"]').click()
        cy.get('[data-test="email-input"]').type('usuario@teste.com')
    })
})
```

**Explicação:**
- `describe`: Define um conjunto de testes
- `it`: Define um teste individual
- `cy`: Objeto do Cypress para interagir com a página
- `data-test`: Atributo usado para localizar elementos

## Boas Práticas

1. **Organização dos Testes**
   - Mantenha os testes organizados em diretórios
   - Use nomes descritivos para os testes
   - Documente os testes adequadamente

2. **Manutenção dos Testes**
   - Atualize os testes quando o sistema mudar
   - Remova testes obsoletos
   - Mantenha as dependências atualizadas

3. **Execução dos Testes**
   - Execute os testes regularmente
   - Mantenha um ambiente de teste separado
   - Documente os resultados dos testes

## Conclusão

Este manual fornece uma base sólida para começar a trabalhar com diferentes tipos de testes. Lembre-se que a prática é essencial para dominar as técnicas de teste. Comece com testes simples e vá aumentando a complexidade conforme ganha experiência.

## Recursos Adicionais

- [Documentação do Selenium](https://www.selenium.dev/documentation/)
- [Documentação do Cypress](https://docs.cypress.io/)
- [Documentação do Locust](https://docs.locust.io/)
- [Documentação do Python unittest](https://docs.python.org/3/library/unittest.html) 