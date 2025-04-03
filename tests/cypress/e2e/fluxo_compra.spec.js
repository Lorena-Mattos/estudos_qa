describe('Fluxo de Compra E2E', () => {
  beforeEach(() => {
    cy.visit('/')
  })

  it('Deve completar uma compra com sucesso', () => {
    // Login
    cy.login('usuario@teste.com', 'senha123')

    // Buscar e adicionar produto
    cy.buscarProduto('Smartphone')
    cy.adicionarAoCarrinho()

    // Ir para o carrinho e aplicar cupom
    cy.get('[data-test="cart-button"]').click()
    cy.aplicarCupom('BLACKFRIDAY')
    cy.get('[data-test="discount-message"]').should('contain', 'Desconto aplicado')

    // Ir para checkout
    cy.get('[data-test="checkout-button"]').click()

    // Preencher endereço
    cy.preencherEndereco({
      rua: 'Rua Teste, 123',
      cidade: 'São Paulo',
      estado: 'SP',
      cep: '01234-567'
    })

    // Selecionar forma de pagamento e preencher cartão
    cy.get('[data-test="payment-method"]').select('Cartão de Crédito')
    cy.preencherCartao({
      numero: '4111111111111111',
      nome: 'João Silva',
      validade: '12/25',
      cvv: '123'
    })

    // Finalizar compra
    cy.get('[data-test="submit-order"]').click()

    // Verificar confirmação
    cy.get('[data-test="order-confirmation"]').should('be.visible')
    cy.get('[data-test="order-number"]').should('not.be.empty')
    cy.get('[data-test="success-message"]').should('contain', 'Compra realizada com sucesso')
  })

  it('Deve mostrar erro ao tentar comprar com carrinho vazio', () => {
    cy.get('[data-test="cart-button"]').click()
    cy.get('[data-test="checkout-button"]').click()
    cy.get('[data-test="error-message"]').should('contain', 'Carrinho vazio')
  })
}) 