# Checklist de Testes Manuais

## 1. Teste de Login

### Cenário: Login com credenciais válidas
- [ ] Acessar a página de login
- [ ] Inserir e-mail válido: teste@email.com
- [ ] Inserir senha válida: 123456
- [ ] Clicar no botão "Entrar"
- [ ] Verificar redirecionamento para página inicial
- [ ] Verificar se o nome do usuário aparece no cabeçalho
- [ ] Verificar se o menu de usuário está disponível

### Cenário: Login com credenciais inválidas
- [ ] Acessar a página de login
- [ ] Inserir e-mail inválido: teste@invalido.com
- [ ] Inserir senha inválida: 123456
- [ ] Clicar no botão "Entrar"
- [ ] Verificar mensagem de erro: "Credenciais inválidas"
- [ ] Verificar se permanece na página de login

## 2. Teste de Busca de Produtos

### Cenário: Busca com resultados
- [ ] Acessar a página inicial
- [ ] Inserir termo de busca: "Smartphone"
- [ ] Clicar no botão de busca
- [ ] Verificar se resultados são exibidos
- [ ] Verificar se os resultados são relevantes
- [ ] Verificar se as imagens dos produtos são exibidas
- [ ] Verificar se os preços são exibidos

### Cenário: Busca sem resultados
- [ ] Acessar a página inicial
- [ ] Inserir termo inexistente: "xyz123"
- [ ] Clicar no botão de busca
- [ ] Verificar mensagem: "Nenhum produto encontrado"
- [ ] Verificar se sugestões são exibidas

## 3. Teste de Carrinho de Compras

### Cenário: Adicionar produto ao carrinho
- [ ] Buscar produto: "Smartphone"
- [ ] Selecionar produto da lista
- [ ] Clicar em "Adicionar ao Carrinho"
- [ ] Verificar mensagem de sucesso
- [ ] Verificar se o ícone do carrinho mostra quantidade
- [ ] Acessar o carrinho
- [ ] Verificar se o produto está listado
- [ ] Verificar se o preço está correto

### Cenário: Remover produto do carrinho
- [ ] Acessar o carrinho
- [ ] Clicar no botão "Remover" do produto
- [ ] Confirmar remoção
- [ ] Verificar se o produto foi removido
- [ ] Verificar se o total foi atualizado
- [ ] Verificar mensagem de carrinho vazio

## 4. Teste de Checkout

### Cenário: Finalizar compra com sucesso
- [ ] Adicionar produto ao carrinho
- [ ] Acessar o carrinho
- [ ] Clicar em "Finalizar Compra"
- [ ] Preencher endereço de entrega
- [ ] Selecionar forma de pagamento: Cartão de Crédito
- [ ] Preencher dados do cartão
- [ ] Clicar em "Confirmar Compra"
- [ ] Verificar página de confirmação
- [ ] Verificar se o número do pedido é exibido
- [ ] Verificar se o e-mail de confirmação foi enviado

### Cenário: Finalizar compra com erro
- [ ] Adicionar produto ao carrinho
- [ ] Acessar o carrinho
- [ ] Clicar em "Finalizar Compra"
- [ ] Preencher endereço de entrega
- [ ] Selecionar forma de pagamento: Cartão de Crédito
- [ ] Preencher dados do cartão com número inválido
- [ ] Clicar em "Confirmar Compra"
- [ ] Verificar mensagem de erro
- [ ] Verificar se permanece na página de pagamento

## 5. Teste de Responsividade

### Cenário: Visualização em Desktop
- [ ] Acessar o site em resolução 1920x1080
- [ ] Verificar layout do menu
- [ ] Verificar tamanho das imagens
- [ ] Verificar espaçamento dos elementos
- [ ] Verificar legibilidade dos textos

### Cenário: Visualização em Mobile
- [ ] Acessar o site em dispositivo móvel
- [ ] Verificar menu hamburguer
- [ ] Verificar tamanho dos botões
- [ ] Verificar rolagem da página
- [ ] Verificar formulários
- [ ] Verificar imagens responsivas

## 6. Teste de Acessibilidade

### Cenário: Navegação por Teclado
- [ ] Navegar usando a tecla Tab
- [ ] Verificar foco dos elementos
- [ ] Verificar ordem de tabulação
- [ ] Verificar atalhos de teclado

### Cenário: Leitores de Tela
- [ ] Ativar leitor de tela
- [ ] Verificar descrições das imagens
- [ ] Verificar textos alternativos
- [ ] Verificar estrutura da página
- [ ] Verificar navegação

## Observações
- Registrar screenshots de problemas encontrados
- Anotar ambiente e configurações utilizadas
- Documentar tempo de execução de cada cenário
- Registrar sugestões de melhorias 