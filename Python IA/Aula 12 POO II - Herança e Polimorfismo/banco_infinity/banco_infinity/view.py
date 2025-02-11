import os
from banco_infinity.banco import Banco
from banco_infinity.conta import Conta


class ContaView:
    def __init__(self, banco: Banco, conta: Conta):
        self.banco = banco
        self.conta = conta
        self.options = {
            'INFO': '1',
            'DEPOSITAR': '2',
            'SACAR': '3',
            'TRANSFERIR': '4',
            'VOLTAR': '5'
        }

    def run(self):
        while True:
            os.system('cls')
            option = self.menu()

            if option == self.options['INFO']:
                self.conta.info()
            elif option == self.options['DEPOSITAR']:
                self.depositar()
            elif option == self.options['SACAR']:
                self.sacar()
            elif option == self.options['TRANSFERIR']:
                self.transferir()
            elif option == self.options['VOLTAR']:
                break
            else:
                print('Opção Inválida.')
        
            input('Aperte <ENTER> para continuar...')

    def menu(self):
        print(f'======= Conta Nº {self.conta.numero} =======')
        print('[1] - Info')
        print('[2] - Depositar')
        print('[3] - Sacar')
        print('[4] - Transferir')
        print('[5] - Voltar')
        print(f'==============================')
        
        option = input('Selecione uma Opção\n--> ')
        return option

    def depositar(self):
        try:
            valor = float(input('Quanto deseja depositar? ')) 
            self.conta.depositar(valor)
        except ValueError as err:
            print(err.args[0])

    def sacar(self):
        try:
            valor = float(input('Quanto deseja sacar? ')) 
            self.conta.sacar(valor)
        except ValueError as err:
            print(err.args[0])

    def transferir(self):
        try:
            numero = input('Para qual conta deseja transferir (Nº da Conta)? ')
            conta_destino = self.banco.buscar_pelo_numero(numero)

            if conta_destino is None:
                raise ValueError('Conta não encontrada.')

            valor = float(input('Quanto deseja transferir? ')) 
            self.conta.transferir(valor, conta_destino)
        except ValueError as err:
            print(err.args[0])


class BancoView:
    def __init__(self, banco: Banco):
        self.banco = banco
        self.options = {
            'CRIAR_CONTA': '1',
            'ENTRAR_CONTA': '2',
            'SAIR': '3'
        }

    def run(self):
        while True:
            os.system('cls')
            option = self.menu()

            if option == self.options['CRIAR_CONTA']:
                self.criar_conta()
            elif option == self.options['ENTRAR_CONTA']:
                self.entrar_conta()
            elif option == self.options['SAIR']:
                break
            else:
                print('Opção Inválida.')

            input('Aperte <ENTER> para continuar...')

    def menu(self) -> str:
        print('======= BANCO INFINITY =======')
        print('[1] - Criar Conta')
        print('[2] - Entrar na Conta')
        print('[3] - Sair')
        print('==============================')

        option = input('Selecione uma Opção\n--> ')
        return option
    
    def criar_conta(self):
        titular = input('Digite o titular da conta: ')
        conta = Conta(titular)

        self.banco.adicionar_conta(conta)
        print('Conta cadastrada com sucesso.')

        conta.info()

    def entrar_conta(self):
        numero = input('Digite o numero da conta: ')
        conta = self.banco.buscar_pelo_numero(numero)

        if conta is None:
            print('Conta não encontrada.')
            return
        
        conta_view = ContaView(self.banco, conta)
        conta_view.run()
