describe('Fluxo de Compra E2E', () => {
  beforeEach(() => {
    // Visitar a página inicial
    cy.visit('https://ecommerce-example.com')
  })

  it('Deve completar uma compra com sucesso', () => {
    // Login
    cy.get('[data-test="login-button"]').click()
    cy.get('[data-test="email-input"]').type('usuario@teste.com')
    cy.get('[data-test="senha-input"]').type('senha123')
    cy.get('[data-test="submit-login"]').click()

    // Buscar produto
    cy.get('[data-test="search-input"]').type('Smartphone')
    cy.get('[data-test="search-button"]').click()

    // Selecionar produto
    cy.get('[data-test="product-list"]').first().click()
    cy.get('[data-test="add-to-cart"]').click()

    // Ir para o carrinho
    cy.get('[data-test="cart-button"]').click()

    // Aplicar cupom
    cy.get('[data-test="coupon-input"]').type('BLACKFRIDAY')
    cy.get('[data-test="apply-coupon"]').click()
    cy.get('[data-test="discount-message"]').should('contain', 'Desconto aplicado')

    // Ir para checkout
    cy.get('[data-test="checkout-button"]').click()

    // Preencher endereço
    cy.get('[data-test="address-input"]').type('Rua Teste, 123')
    cy.get('[data-test="city-input"]').type('São Paulo')
    cy.get('[data-test="state-input"]').type('SP')
    cy.get('[data-test="zip-input"]').type('01234-567')

    // Selecionar forma de pagamento
    cy.get('[data-test="payment-method"]').select('Cartão de Crédito')
    cy.get('[data-test="card-number"]').type('4111111111111111')
    cy.get('[data-test="card-name"]').type('João Silva')
    cy.get('[data-test="card-expiry"]').type('12/25')
    cy.get('[data-test="card-cvv"]').type('123')

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