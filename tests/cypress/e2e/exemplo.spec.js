describe('Exemplo de Teste E2E', () => {
  it('Deve testar interações com formulários', () => {
    // Visitar a página inicial
    cy.visit('/')

    // Clicar no link "type" e esperar a página carregar
    cy.contains('type').click()
    cy.wait(1000) // Espera 1 segundo para a página carregar

    // Testar campo de e-mail
    cy.get('#email1')
      .type('teste@exemplo.com')
      .should('have.value', 'teste@exemplo.com')

    // Testar campo de senha
    cy.get('#password1')
      .type('senha123')
      .should('have.value', 'senha123')

    // Testar campo desabilitado
    cy.get('.action-disabled')
      .type('texto desabilitado', { force: true })
      .should('have.value', 'texto desabilitado')

    // Testar foco
    cy.get('.action-focus').focus()
    cy.get('.action-focus').should('have.class', 'focus')

    // Testar blur
    cy.get('.action-blur')
      .type('Texto para blur')
      .blur()
    cy.get('.action-blur').should('have.class', 'error')

    // Testar clear
    cy.get('.action-clear')
      .type('Texto para limpar')
      .should('have.value', 'Texto para limpar')
      .clear()
      .should('have.value', '')
  })

  it('Deve testar interações com checkboxes e selects', () => {
    // Visitar a página inicial
    cy.visit('/')

    // Clicar no link "type" e esperar a página carregar
    cy.contains('type').click()
    cy.wait(1000) // Espera 1 segundo para a página carregar

    // Testar checkboxes
    cy.get('.action-checkboxes [type="checkbox"]')
      .not('[disabled]')
      .check()
      .should('be.checked')

    // Testar radios
    cy.get('.action-radios [type="radio"]')
      .not('[disabled]')
      .check('radio1')
      .should('be.checked')

    // Testar select
    cy.get('.action-select')
      .select('apples')
      .should('have.value', 'fr-apples')

    // Testar select múltiplo
    cy.get('.action-select-multiple')
      .select(['apples', 'oranges', 'bananas'])
      .invoke('val')
      .should('deep.equal', ['fr-apples', 'fr-oranges', 'fr-bananas'])
  })

  it('Deve testar scroll e cliques', () => {
    // Visitar a página inicial
    cy.visit('/')

    // Clicar no link "type" e esperar a página carregar
    cy.contains('type').click()
    cy.wait(1000) // Espera 1 segundo para a página carregar

    // Testar scroll
    cy.get('#scroll-vertical button')
      .should('not.be.visible')
      .scrollIntoView()
      .should('be.visible')

    // Testar cliques em diferentes posições
    cy.get('#action-canvas')
      .click('topLeft')
      .click('top')
      .click('topRight')
      .click('left')
      .click('right')
      .click('bottomLeft')
      .click('bottom')
      .click('bottomRight')

    // Testar clique com coordenadas
    cy.get('#action-canvas')
      .click(80, 75)
      .click(170, 75)
      .click(80, 165)
  })
}) 