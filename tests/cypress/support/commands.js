// Comandos personalizados para login
Cypress.Commands.add('login', (email, senha) => {
  cy.get('[data-test="login-button"]').click()
  cy.get('[data-test="email-input"]').type(email)
  cy.get('[data-test="senha-input"]').type(senha)
  cy.get('[data-test="submit-login"]').click()
})

// Comandos personalizados para busca de produto
Cypress.Commands.add('buscarProduto', (termo) => {
  cy.get('[data-test="search-input"]').type(termo)
  cy.get('[data-test="search-button"]').click()
})

// Comandos personalizados para adicionar ao carrinho
Cypress.Commands.add('adicionarAoCarrinho', () => {
  cy.get('[data-test="product-list"]').first().click()
  cy.get('[data-test="add-to-cart"]').click()
})

// Comandos personalizados para aplicar cupom
Cypress.Commands.add('aplicarCupom', (codigo) => {
  cy.get('[data-test="coupon-input"]').type(codigo)
  cy.get('[data-test="apply-coupon"]').click()
})

// Comandos personalizados para preencher endereço
Cypress.Commands.add('preencherEndereco', (endereco) => {
  cy.get('[data-test="address-input"]').type(endereco.rua)
  cy.get('[data-test="city-input"]').type(endereco.cidade)
  cy.get('[data-test="state-input"]').type(endereco.estado)
  cy.get('[data-test="zip-input"]').type(endereco.cep)
})

// Comandos personalizados para preencher cartão
Cypress.Commands.add('preencherCartao', (cartao) => {
  cy.get('[data-test="card-number"]').type(cartao.numero)
  cy.get('[data-test="card-name"]').type(cartao.nome)
  cy.get('[data-test="card-expiry"]').type(cartao.validade)
  cy.get('[data-test="card-cvv"]').type(cartao.cvv)
})