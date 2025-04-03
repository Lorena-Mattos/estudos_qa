import './commands';


// Configurações globais
Cypress.on('uncaught:exception', (err, runnable) => {
  // Retornar false para evitar que o Cypress falhe no teste
  return false
})

// Configurações de viewport
Cypress.config('viewportWidth', 1280)
Cypress.config('viewportHeight', 720) 