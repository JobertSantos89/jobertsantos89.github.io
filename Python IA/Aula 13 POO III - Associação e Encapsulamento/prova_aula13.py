class ContaBancaria:
    def __init__(self, titular: str, saldo: float = 0.0):
        """
        Construtor da classe ContaBancaria.
        :param titular: Nome do titular da conta (str).
        :param saldo_inicial: Saldo inicial da conta (float, opcional, padrão é 0).
        """
        self._titular = titular  # Atributo privado para o titular
        self._saldo = saldo  # Atributo privado para o saldo

    def depositar(self, valor):
        """
        Adiciona um valor ao saldo da conta.
        :param valor: Valor a ser depositado (float).
        """
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Erro: O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        """
        Retira um valor do saldo da conta, se houver saldo suficiente.
        :param valor: Valor a ser sacado (float).
        """
        if valor > 0:
            if self._saldo >= valor:
                self._saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            else:
                print("Erro: Saldo insuficiente para realizar o saque.")
        else:
            print("Erro: O valor do saque deve ser positivo.")

    def exibir_saldo(self):
        """
        Exibe o saldo atual da conta.
        """
        print(f"Saldo atual da conta de {self._titular}: R${self._saldo:.2f}")

    # Métodos getters para acessar os atributos privados (opcional)
    def get_titular(self):
        """
        Retorna o nome do titular da conta.
        :return: Nome do titular (str).
        """
        return self._titular

    def get_saldo(self):
        """
        Retorna o saldo atual da conta.
        :return: Saldo atual (float).
        """
        return self._saldo