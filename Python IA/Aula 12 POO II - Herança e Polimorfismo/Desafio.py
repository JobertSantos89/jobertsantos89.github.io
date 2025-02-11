class Conta:
    """Classe base para contas bancárias"""
    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        """Método para depositar dinheiro na conta"""
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        """Método para saque padrão"""
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def resumo(self):
        """Método polimórfico que exibe os detalhes da conta"""
        return f"Conta: {self.numero} | Titular: {self.titular} | Saldo: R${self.saldo:.2f}"

class ContaCorrente(Conta):
    """Classe que representa uma conta corrente"""
    def __init__(self, numero, titular, saldo=0, taxa_manutencao=10, cheque_especial=500):
        super().__init__(numero, titular, saldo)
        self.taxa_manutencao = taxa_manutencao
        self.cheque_especial = cheque_especial

    def sacar(self, valor):
        """Sobrescrevendo o método de saque para considerar o cheque especial"""
        limite_total = self.saldo + self.cheque_especial
        if 0 < valor <= limite_total:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso! (Cheque especial disponível: R${self.cheque_especial:.2f})")
        else:
            print("Saldo insuficiente, mesmo com cheque especial.")

    def resumo(self):
        """Resumo específico para conta corrente"""
        return f"[Conta Corrente] {super().resumo()} | Cheque Especial: R${self.cheque_especial:.2f}"

class ContaPoupanca(Conta):
    """Classe que representa uma conta poupança"""
    def __init__(self, numero, titular, saldo=0, taxa_juros=0.02):
        super().__init__(numero, titular, saldo)
        self.taxa_juros = taxa_juros

    def adicionar_juros(self):
        """Aplica juros ao saldo"""
        juros = self.saldo * self.taxa_juros
        self.saldo += juros
        print(f"Juros de R${juros:.2f} aplicados! Novo saldo: R${self.saldo:.2f}")

    def resumo(self):
        """Resumo específico para conta poupança"""
        return f"[Conta Poupança] {super().resumo()} | Taxa de Juros: {self.taxa_juros * 100:.2f}%"

# ======================= TESTE DE FUNCIONALIDADE =======================

# Criando contas
conta_corrente = ContaCorrente(numero="12345", titular="João", saldo=1000)
conta_poupanca = ContaPoupanca(numero="12345", titular="João", saldo=1000)

# Testando operações
print("\n💰 REALIZANDO OPERAÇÕES BANCÁRIAS 💰\n")

# Depósitos
conta_corrente.depositar(500)
conta_poupanca.depositar(300)

# Saques
conta_corrente.sacar(1800)  # Testando cheque especial
conta_poupanca.sacar(2500)  # Saldo insuficiente

# Adicionando juros na poupança
conta_poupanca.adicionar_juros()

# Exibindo resumos
print("\n📄 RESUMO DAS CONTAS 📄\n")
print(conta_corrente.resumo())
print(conta_poupanca.resumo())