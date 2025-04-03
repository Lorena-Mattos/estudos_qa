from locust import HttpUser, task, between
import random

class UsuarioEcommerce(HttpUser):
    wait_time = between(1, 3)  # Tempo de espera entre requisições
    
    def on_start(self):
        # Login do usuário
        self.client.post("/login", {
            "email": "usuario@teste.com",
            "senha": "senha123"
        })
    
    @task(3)  # Peso 3: mais frequente
    def ver_produtos(self):
        self.client.get("/produtos")
        
    @task(2)  # Peso 2: frequência média
    def buscar_produto(self):
        termos = ["smartphone", "notebook", "tv", "geladeira"]
        termo = random.choice(termos)
        self.client.get(f"/busca?q={termo}")
        
    @task(1)  # Peso 1: menos frequente
    def adicionar_carrinho(self):
        # Simular adição de produto ao carrinho
        produto_id = random.randint(1, 100)
        self.client.post("/carrinho/adicionar", {
            "produto_id": produto_id,
            "quantidade": 1
        })
        
    @task(1)
    def finalizar_compra(self):
        # Simular finalização de compra
        self.client.post("/checkout", {
            "endereco": "Rua Teste, 123",
            "forma_pagamento": "cartao",
            "numero_cartao": "4111111111111111",
            "data_validade": "12/25",
            "cvv": "123"
        }) 