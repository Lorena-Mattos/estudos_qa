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