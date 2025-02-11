import os
from banco_infinity.conta import Conta


class Banco:
    def __init__(self, contas: list[Conta] = []):
        self.contas = contas

    def buscar_pelo_numero(self, numero: str) -> Conta | None:
        for conta in self.contas:
            if conta.numero == numero:
                return conta
            
        return None

    def adicionar_conta(self, conta: Conta):
        self.contas.append(conta)