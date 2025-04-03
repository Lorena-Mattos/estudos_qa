import random
from dataclasses import dataclass

@dataclass
class ResultadoPagamento:
    sucesso: bool
    valor: float
    codigo_transacao: str = None
    mensagem_erro: str = None

class SistemaDePagamento:
    def processar_pagamento(self, carrinho, numero_cartao, nome_titular, data_validade, cvv):
        # Validação básica do cartão
        if not self._validar_cartao(numero_cartao):
            return ResultadoPagamento(
                sucesso=False,
                valor=carrinho.calcular_total(),
                mensagem_erro="Cartão inválido"
            )
            
        # Simular processamento do pagamento
        valor_total = carrinho.calcular_total()
        codigo_transacao = f"TRX{random.randint(100000, 999999)}"
        
        return ResultadoPagamento(
            sucesso=True,
            valor=valor_total,
            codigo_transacao=codigo_transacao
        )
        
    def _validar_cartao(self, numero_cartao):
        # Simulação de validação de cartão
        # Em um sistema real, isso seria mais complexo
        return numero_cartao.startswith("4")  # Apenas cartões que começam com 4 são válidos 