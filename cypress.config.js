const { defineConfig } = require('cypress')
 
 module.exports = defineConfig({
  e2e: {
    baseUrl: 'https://example.cypress.io',
    specPattern: 'tests/cypress/e2e/**/*.spec.js',
    supportFile: false, // Desativa o suporte a arquivos globais
    fixturesFolder: 'tests/cypress/fixtures',
    downloadsFolder: 'tests/cypress/downloads',
    video: true,
    screenshotOnRunFailure: true
  }
});