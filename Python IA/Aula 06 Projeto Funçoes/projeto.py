import os #importar módulos
import random as rd
from tabulate import tabulate

clientes = []

def menu():
    print('========= Loja de Doces =========')
    print('[1] - Listar Vendas')
    print('[2] - Registrar Nova Venda')
    print('[3] - Encerrar')
    print('=================================')

    while True:
        option = input('Selecione uma opção -> ')

        if option in ('1', '2', '3'):
            break

        print('Opção inválida, digite novamente.')
    
    return option

def listar_clientes():
    print(clientes)

def registrar_cliente():
    cliente = {}

    cliente['nome'] = input('Digite o nome do cliente: ')
    cliente['telefone'] = input('Digite o telefone do cliente: ')
    cliente['endereco'] = input('Digite o endereco do cliente: ')

    return cliente

def sortear():
    pass

# Código principal.
def main():
    while True:
        opcao = menu()

        if opcao == '1':
            listar_clientes()
        elif opcao == '2':
            cliente = registrar_cliente()
            clientes.append(cliente)
        elif opcao == '3':
            cliente = sortear()
            print('O cliente sorteado foi...')
            break

    print('Fim do Programa')


if __name__ == '__main__':
    main()