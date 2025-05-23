# Exemplos Práticos de Testes QA

Este projeto contém exemplos práticos dos diferentes tipos de testes que um QA realiza no dia a dia.

## Documentação

- [Manual Completo de Testes](manual_testes.md) - Guia detalhado com explicações passo a passo de cada tipo de teste
- [Guia de Execução de Testes](docs/execucao_testes.md) - Instruções para configurar e executar os diferentes tipos de testes

## Estrutura do Projeto

```
.
├── src/                    # Código fonte da aplicação
├── tests/                  # Testes
│   ├── manual/            # Exemplos de testes manuais
│   ├── automated/         # Testes automatizados
│   ├── unit/              # Testes de unidade
│   ├── integration/       # Testes de integração
│   ├── functional/        # Testes funcionais
│   ├── regression/        # Testes de regressão
│   ├── load/              # Testes de carga
│   └── e2e/               # Testes end-to-end
└── docs/                  # Documentação
```

## Exemplos de Testes

### 1. Testes Manuais
**Cenário**: Teste de login em um e-commerce
- Abrir o navegador e acessar a página de login
- Inserir credenciais válidas (usuário: teste@email.com, senha: 123456)
- Verificar se o login é bem-sucedido
- Verificar se o usuário é redirecionado para a página inicial
- Verificar se o nome do usuário aparece no cabeçalho

### 2. Testes Automatizados
**Cenário**: Teste automatizado de adição ao carrinho
```python
def test_add_to_cart():
    # Abrir navegador
    driver = webdriver.Chrome()
    driver.get("https://ecommerce.com")
    
    # Buscar produto
    search_box = driver.find_element(By.ID, "search")
    search_box.send_keys("Smartphone")
    search_box.submit()
    
    # Adicionar ao carrinho
    add_to_cart_button = driver.find_element(By.CLASS_NAME, "add-to-cart")
    add_to_cart_button.click()
    
    # Verificar mensagem de sucesso
    assert "Produto adicionado ao carrinho" in driver.page_source
```

### 3. Testes de Unidade
**Cenário**: Teste da classe CarrinhoDeCompras
```python
def test_calcular_total_carrinho():
    carrinho = CarrinhoDeCompras()
    carrinho.adicionar_item(Produto("Smartphone", 1000))
    carrinho.adicionar_item(Produto("Capa", 50))
    
    assert carrinho.calcular_total() == 1050
```

### 4. Testes de Integração
**Cenário**: Teste da integração entre Carrinho e Pagamento
```python
def test_processar_pagamento():
    carrinho = CarrinhoDeCompras()
    pagamento = SistemaDePagamento()
    
    carrinho.adicionar_item(Produto("Smartphone", 1000))
    resultado = pagamento.processar_pagamento(carrinho, "1234567890123456")
    
    assert resultado.sucesso == True
    assert carrinho.esta_vazio() == True
```

### 5. Testes Funcionais
**Cenário**: Teste do fluxo completo de compra
1. Login do usuário
2. Busca de produto
3. Adição ao carrinho
4. Aplicação de cupom de desconto
5. Seleção de método de pagamento
6. Confirmação da compra
7. Verificação do e-mail de confirmação

### 6. Testes de Regressão
**Cenário**: Verificação após atualização do sistema de pagamento
- Testar todas as formas de pagamento existentes
- Verificar se os descontos ainda funcionam
- Confirmar se o processamento de cartões continua funcionando
- Validar se as notificações de pagamento são enviadas

### 7. Testes de Carga
**Cenário**: Teste de performance durante Black Friday
```python
def test_carga_simultanea():
    # Simular 1000 usuários acessando simultaneamente
    with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as executor:
        futures = [executor.submit(realizar_compra) for _ in range(1000)]
        resultados = [f.result() for f in futures]
    
    # Verificar tempos de resposta
    assert all(r.tempo_resposta < 2.0 for r in resultados)
```

### 8. Testes End-to-End (E2E)
**Cenário**: Fluxo completo de compra com Cypress
```javascript
describe('Fluxo de Compra', () => {
  it('Deve completar uma compra com sucesso', () => {
    cy.visit('/')
    cy.login('usuario@teste.com', 'senha123')
    cy.buscarProduto('Smartphone')
    cy.adicionarAoCarrinho()
    cy.irParaCarrinho()
    cy.aplicarCupom('BLACKFRIDAY')
    cy.selecionarPagamento('cartao')
    cy.preencherDadosCartao()
    cy.confirmarCompra()
    cy.verificarEmailConfirmacao()
  })
})
```

## Outros Tipos de Testes Importantes

### 9. Testes de Segurança
**Cenário**: Teste de vulnerabilidades comuns
- Teste de injeção SQL
- Verificação de XSS (Cross-Site Scripting)
- Validação de autenticação
- Teste de permissões de acesso

### 10. Testes de Usabilidade
**Cenário**: Avaliação da experiência do usuário
- Tempo para completar tarefas comuns
- Facilidade de navegação
- Clareza das mensagens de erro
- Acessibilidade (WCAG)

### 11. Testes de Compatibilidade
**Cenário**: Verificação em diferentes ambientes
- Teste em diferentes navegadores (Chrome, Firefox, Safari)
- Teste em diferentes dispositivos (desktop, mobile, tablet)
- Teste em diferentes sistemas operacionais
- Teste em diferentes resoluções de tela

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

A licença MIT é uma licença de software livre que permite que qualquer pessoa use, copie, modifique, mescle, publique, distribua, sublicencie e/ou venda cópias do software, desde que inclua o aviso de copyright e a permissão em todas as cópias ou partes substanciais do software.

### O que você pode fazer com este projeto:
- Usar em projetos comerciais
- Modificar e adaptar para suas necessidades
- Distribuir versões modificadas
- Usar em projetos privados

### O que você deve fazer:
- Manter o aviso de copyright original
- Incluir uma cópia da licença MIT
- Dar crédito aos autores originais

## Como Colaborar

Este projeto é aberto para contribuições da comunidade. Se você quiser contribuir, siga estas etapas:

1. **Fork do Projeto**
   - Faça um fork do repositório no GitHub
   - Clone o fork para sua máquina local

2. **Criar uma Branch**
   ```bash
   git checkout -b feature/nova-funcionalidade
   ```

3. **Fazer as Alterações**
   - Adicione novos exemplos de testes
   - Melhore a documentação existente
   - Corrija erros ou bugs
   - Adicione novos tipos de testes

4. **Commit das Alterações**
   ```bash
   git commit -m "Adiciona exemplo de teste de segurança"
   ```

5. **Push para o Fork**
   ```bash
   git push origin feature/nova-funcionalidade
   ```

6. **Abrir um Pull Request**
   - Vá para o repositório original no GitHub
   - Clique em "New Pull Request"
   - Selecione sua branch
   - Descreva suas alterações
   - Aguarde a revisão

### Tipos de Contribuições Bem-vindas:
- **Documentação**
  - Melhorar explicações existentes
  - Adicionar mais exemplos
  - Traduzir para outros idiomas

- **Código**
  - Adicionar novos tipos de testes
  - Melhorar exemplos existentes
  - Adicionar testes para novas tecnologias

- **Issues**
  - Reportar bugs
  - Sugerir melhorias
  - Pedir ajuda com dúvidas

### Boas Práticas para Contribuições:
1. Siga o padrão de código existente
2. Documente suas alterações
3. Adicione testes para novas funcionalidades
4. Mantenha os commits pequenos e focados
5. Escreva mensagens de commit claras

### Precisa de Ajuda?
- Abra uma issue no GitHub
- Participe das discussões
- Consulte a documentação
- Entre em contato com os mantenedores


