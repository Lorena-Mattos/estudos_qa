import React from 'react'
import { mount } from '@cypress/react'
import Button from './Button' // Componente que será testado

describe('Teste do Componente Button', () => {
  it('Deve renderizar o botão com texto correto', () => {
    mount(<Button>Clique Aqui</Button>)
    cy.get('button').should('have.text', 'Clique Aqui')
  })

  it('Deve aplicar a classe correta quando desabilitado', () => {
    mount(<Button disabled>Botão Desabilitado</Button>)
    cy.get('button')
      .should('be.disabled')
      .and('have.class', 'disabled')
  })

  it('Deve chamar a função onClick quando clicado', () => {
    const onClick = cy.stub()
    mount(<Button onClick={onClick}>Clique Aqui</Button>)
    cy.get('button').click()
    cy.wrap(onClick).should('have.been.calledOnce')
  })

  it('Deve renderizar com diferentes variantes', () => {
    mount(
      <div>
        <Button variant="primary">Primário</Button>
        <Button variant="secondary">Secundário</Button>
        <Button variant="danger">Perigo</Button>
      </div>
    )
    
    cy.get('button').first().should('have.class', 'primary')
    cy.get('button').eq(1).should('have.class', 'secondary')
    cy.get('button').last().should('have.class', 'danger')
  })

  it('Deve mostrar loading state', () => {
    mount(<Button loading>Carregando</Button>)
    cy.get('button')
      .should('have.class', 'loading')
      .and('be.disabled')
    cy.get('.spinner').should('be.visible')
  })

  it('Deve renderizar ícone quando fornecido', () => {
    mount(<Button icon="check">Com Ícone</Button>)
    cy.get('.icon').should('be.visible')
    cy.get('button').should('have.class', 'has-icon')
  })
}) 