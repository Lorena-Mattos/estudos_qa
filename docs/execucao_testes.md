# Guia de Execução de Testes

Este documento explica como executar os diferentes tipos de testes no projeto.

## Pré-requisitos

- Python 3.8+
- Node.js 14+
- Chrome/Chromium instalado
- Selenium WebDriver
- Locust
- Cypress

## Instalação das Dependências

```bash
# Python
pip install -r requirements.txt

# Node.js
npm install
```

## Configuração do Cypress

### 1. Instalação Inicial

```bash
# Instalar o Cypress como dependência de desenvolvimento
npm install cypress --save-dev
```

### 2. Estrutura de Arquivos

Após a instalação, o Cypress criará a seguinte estrutura de diretórios:

```
cypress/
├── e2e/           # Arquivos de teste
├── fixtures/      # Dados de teste
├── support/       # Arquivos de suporte
│   ├── commands.js  # Comandos personalizados
│   └── e2e.js       # Configurações globais
└── downloads/     # Arquivos baixados durante os testes
```

### 3. Configuração do Cypress

#### 3.1 Primeira Execução
Ao abrir o Cypress pela primeira vez, você verá duas opções:

1. **E2E Testing**
   - Clique em "E2E Testing" para testar a aplicação completa
   - O Cypress criará a estrutura básica de arquivos
   - Escolha o navegador (Chrome, Edge, etc.)
   - Clique em "Start E2E Testing in Chrome"

2. **Component Testing**
   - Clique em "Component Testing" para testar componentes isolados
   - O Cypress criará a estrutura para testes de componentes
   - Escolha o framework (React, Vue, etc.)
   - Configure o bundler (Webpack, Vite)
   - Clique em "Next Step"

#### 3.2 Configuração do Projeto

Para manter a organização do projeto de estudos, vamos usar a seguinte estrutura:

```
projeto/
├── tests/
│   ├── cypress/              # Testes do Cypress
│   │   ├── e2e/              # Testes end-to-end
│   │   │   ├── fluxo_compra.spec.js
│   │   │   └── login.spec.js
│   │   ├── component/        # Testes de componentes
│   │   │   ├── button.spec.js
│   │   │   └── form.spec.js
│   │   ├── support/          # Arquivos de suporte
│   │   │   ├── commands.js
│   │   │   ├── e2e.js
│   │   │   └── component.js
│   │   ├── fixtures/         # Dados de teste
│   │   └── downloads/        # Arquivos baixados
│   ├── selenium/             # Testes Selenium
│   ├── unit/                 # Testes de unidade
│   └── integration/          # Testes de integração
├── cypress.config.js
└── package.json
```

#### 3.3 Configuração do Cypress para E2E Testing

1. **Criar o arquivo de configuração:**
```javascript
// cypress.config.js
const { defineConfig } = require('cypress')

module.exports = defineConfig({
  e2e: {
    baseUrl: 'http://localhost:3000',
    specPattern: 'tests/cypress/e2e/**/*.spec.js', // Note o caminho atualizado
    supportFile: 'tests/cypress/support/e2e.js',
    viewportWidth: 1280,
    viewportHeight: 720,
    defaultCommandTimeout: 5000,
    video: false,
  }
})
```

2. **Executar testes E2E:**
```bash
# Abrir o Cypress no modo E2E
npx cypress open --e2e

# Executar testes E2E no modo headless
npx cypress run --e2e
```

#### 3.4 Configuração do Cypress para Component Testing

1. **Criar o arquivo de configuração:**
```javascript
// cypress.config.js
const { defineConfig } = require('cypress')

module.exports = defineConfig({
  component: {
    devServer: {
      framework: 'react', // ou 'vue', 'angular', etc.
      bundler: 'webpack', // ou 'vite'
    },
    specPattern: 'tests/cypress/component/**/*.spec.js', // Note o caminho atualizado
    supportFile: 'tests/cypress/support/component.js',
  }
})
```

2. **Executar testes de Componentes:**
```bash
# Abrir o Cypress no modo Component
npx cypress open --component

# Executar testes de Componentes no modo headless
npx cypress run --component
```

#### 3.5 Dicas para Configuração

1. **E2E Testing:**
   - Configure a `baseUrl` correta para sua aplicação
   - Ajuste os timeouts conforme necessário
   - Use fixtures para dados de teste
   - Configure hooks globais no `e2e.js`

2. **Component Testing:**
   - Escolha o framework correto
   - Configure o bundler adequado
   - Use mocks para dependências externas
   - Configure o ambiente de teste no `component.js`

### 4. Diferenças entre E2E e Component Testing

| Característica | E2E Testing | Component Testing |
|----------------|-------------|-------------------|
| Escopo | Aplicação completa | Componentes individuais |
| Velocidade | Mais lento | Mais rápido |
| Configuração | Mais simples | Requer configuração do framework |
| Isolamento | Menos isolado | Totalmente isolado |
| Uso | Testes de fluxo | Desenvolvimento de componentes |
| Dependências | Todas carregadas | Apenas necessárias |

### 5. Quando Escolher Cada Tipo

**Escolha E2E quando:**
- Estiver testando fluxos completos
- Precisar simular interações do usuário
- Testar integração entre componentes
- Validar funcionalidades end-to-end

**Escolha Component Testing quando:**
- Desenvolver componentes isoladamente
- Precisar de feedback rápido durante o desenvolvimento
- Testar lógica específica de componentes
- Validar props e estados

### 6. Comandos Personalizados

No arquivo `cypress/support/commands.js`, você pode adicionar comandos personalizados:

```javascript
Cypress.Commands.add('login', (email, senha) => {
  cy.get('#email').type(email)
  cy.get('#senha').type(senha)
  cy.get('#btn-login').click()
})
```

### 7. Configurações Globais

No arquivo `cypress/support/e2e.js`, adicione configurações globais:

```javascript
// Importar comandos personalizados
import './commands'

// Configurar hooks globais
beforeEach(() => {
  cy.clearCookies()
  cy.clearLocalStorage()
})
```

### 8. Executando os Testes

```bash
# Abrir o Cypress no modo interativo
npx cypress open

# Executar testes no modo headless
npx cypress run

# Executar um arquivo específico
npx cypress run --spec "cypress/e2e/exemplo.spec.js"
```

### 9. Dicas de Configuração

1. **Timeouts**: Ajuste os timeouts conforme necessário:
   ```javascript
   {
     defaultCommandTimeout: 10000,
     pageLoadTimeout: 60000,
     responseTimeout: 30000
   }
   ```

2. **Ambientes**: Configure diferentes ambientes:
   ```javascript
   {
     env: {
       dev: 'http://localhost:3000',
       staging: 'http://staging.example.com',
       prod: 'http://example.com'
     }
   }
   ```

3. **Reporter**: Configure relatórios de teste:
   ```bash
   npm install mochawesome --save-dev
   ```

4. **Variáveis de Ambiente**: Use arquivo `.env`:
   ```bash
   CYPRESS_API_URL=http://api.example.com
   CYPRESS_USERNAME=teste
   CYPRESS_PASSWORD=senha123
   ```

### 10. Boas Práticas

1. **Organização**:
   - Separe os testes por funcionalidade
   - Use nomes descritivos para os arquivos
   - Mantenha os seletores em um arquivo separado

2. **Manutenção**:
   - Atualize os seletores quando o HTML mudar
   - Mantenha os testes independentes
   - Use fixtures para dados de teste

3. **Performance**:
   - Evite esperas fixas (cy.wait)
   - Use comandos assíncronos quando possível
   - Limpe cookies e localStorage entre testes

### 11. Recursos de Aprendizado

1. **Documentação Oficial**:
   - [Documentação do Cypress](https://docs.cypress.io/guides/overview/why-cypress)
   - [Guia de Comandos](https://docs.cypress.io/api/commands)
   - [Exemplos de Testes](https://docs.cypress.io/examples/examples/recipes)

2. **Cursos e Tutoriais**:
   - [Curso Gratuito da Escola TAT](https://www.udemy.com/course/testes-automatizados-com-cypress-basico/)
   - [Curso da Alura](https://www.alura.com.br/curso-online-cypress-automacao-de-testes)
   - [Curso da Udemy](https://www.udemy.com/course/cypress-avancado/)

3. **Blogs e Artigos**:
   - [Blog do Cypress](https://www.cypress.io/blog/)
   - [Talking About Testing](https://talkingabouttesting.com/)
   - [QA Ninja](https://qaninja.io/)

4. **Vídeos e Playlists**:
   - [Canal do Cypress no YouTube](https://www.youtube.com/c/Cypressio)
   - [Playlist de Cypress da Escola TAT](https://www.youtube.com/playlist?list=PLjSmq4XqHkGz4XqQqQwU5j5x3tJgJ8wYF)
   - [Playlist de Cypress da Alura](https://www.youtube.com/playlist?list=PLh2Y_pKOa4Uf-cUQOvZ1OLwHr9g9t9X2p)

5. **Comunidades**:
   - [Discord do Cypress](https://discord.gg/cypress)
   - [Grupo do Telegram QA Brasil](https://t.me/qabrasil)
   - [Fórum do Cypress](https://github.com/cypress-io/cypress/discussions)

6. **Projetos de Exemplo**:
   - [Cypress Real World App](https://github.com/cypress-io/cypress-realworld-app)
   - [Cypress Examples](https://github.com/cypress-io/cypress-example-kitchensink)
   - [Cypress Best Practices](https://github.com/cypress-io/cypress-example-recipes)

7. **Ferramentas Úteis**:
   - [Cypress Dashboard](https://dashboard.cypress.io/)
   - [Cypress Studio](https://docs.cypress.io/guides/core-concepts/cypress-studio)
   - [Cypress Testing Library](https://github.com/testing-library/cypress-testing-library)

8. **Extensões do VS Code**:
   - [Cypress Helper](https://marketplace.visualstudio.com/items?itemName=Shelex.vscode-cy-helper)
   - [Cypress Snippets](https://marketplace.visualstudio.com/items?itemName=andrew-codes.cypress-snippets)
   - [Cypress Test Runner](https://marketplace.visualstudio.com/items?itemName=cypress-io.cypress-test-runner)

## Testes Automatizados (Selenium)

```bash
python -m unittest tests/automated/test_login.py
```

## Testes de Unidade

```bash
python -m unittest tests/unit/test_carrinho.py
```

## Testes de Integração

```bash
python -m unittest tests/integration/test_pagamento.py
```

## Testes de Carga (Locust)

1. Inicie o servidor de teste:
```bash
locust -f tests/load/test_carga.py
```

2. Acesse http://localhost:8089 no navegador
3. Configure o número de usuários e taxa de spawn
4. Inicie o teste

## Testes End-to-End (Cypress)

1. Abra o Cypress:
```bash
npx cypress open
```

2. Selecione o arquivo de teste `tests/e2e/fluxo_compra.spec.js`

## Testes Manuais

Os testes manuais devem ser executados seguindo os casos de teste documentados no README.md. Cada passo deve ser seguido manualmente e os resultados devem ser registrados.

## Dicas para Execução

1. **Testes Automatizados**:
   - Certifique-se de que o ChromeDriver está na PATH
   - Verifique se o site de teste está acessível

2. **Testes de Carga**:
   - Ajuste os parâmetros de teste conforme a capacidade do servidor
   - Monitore os recursos do servidor durante o teste

3. **Testes E2E**:
   - Use o modo headless para execução em CI/CD
   - Configure timeouts adequados para cada ambiente

4. **Testes Manuais**:
   - Documente cada passo executado
   - Registre screenshots de problemas encontrados
   - Anote o ambiente e configurações utilizadas 