class ContaBancaria:
    def __init__(self, titular: str, saldo: float = 0.0):
        self._titular = titular
        self._saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Erro: O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0:
            if self._saldo >= valor:
                self._saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            else:
                print("Erro: Saldo insuficiente para realizar o saque.")
        else:
            print("Erro: O valor do saque deve ser positivo.")

    def exibir_saldo(self):
        print(f"Saldo atual da conta de {self._titular}: R${self._saldo:.2f}")

    def get_titular(self):
        return self._titular

    def get_saldo(self):
        return self._saldo


def main():
    conta = ContaBancaria("Jobert Santos", 100.0)
    conta.exibir_saldo()
    conta.depositar(50.0)
    conta.exibir_saldo()
    conta.sacar(30.0)
    conta.exibir_saldo()
    conta.sacar(150.0)
    conta.exibir_saldo()
    conta.depositar(-20.0)
    conta.sacar(-10.0)


if __name__ == "__main__":
    main()
    def get_saldo(self):
        """
        Retorna o saldo atual da conta.
        :return: Saldo atual (float).
        """
        return self._saldo
