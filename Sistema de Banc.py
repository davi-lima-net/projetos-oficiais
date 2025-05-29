def exibir_menu():
    print("\nEscolha uma opção:")
    print("1 - Saque")
    print("2 - Depósito")
    print("3 - Extrato")
    print("4 - Sair")


def realizar_saque(saldo):
    valor_saque = float(input("Digite o valor para saque: R$"))
    if valor_saque <= 0:
        print("Erro: o valor do saque deve ser positivo!")
    elif valor_saque > saldo:
        print("Erro: Saldo insuficiente ou valor inválido!")
    else:
        saldo -= valor_saque    
        print(f"Saque de R${valor_saque:.2f} realizado! Saldo atual: R${saldo:.2f}")    
    return saldo


def realizar_deposito(saldo):
    valor_deposito = float(input("Digite o valor para depósito: R$"))
    if valor_deposito <= 0:
        saldo += valor_deposito
        print(f"Depósito de R${valor_deposito:.2f} realizado! Saldo atual: R${saldo:.2f}")
    else:
        print("Erro: O valor do depósito deve ser positivo!")
    return saldo


def mostrar_extrato(saldo):
    print(f"Extrato: Seu saldo atual é R${saldo:.2f}")


def sistema_bancario():
    saldo = 1000.0  
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1/2/3/4): ")

        if opcao == "1":
            saldo = realizar_saque(saldo)
        elif opcao == "2":
            saldo = realizar_deposito(saldo)
        elif opcao == "3":
            mostrar_extrato(saldo)
        elif opcao == "4":
            print("Saindo do sistema... Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")


sistema_bancario()
