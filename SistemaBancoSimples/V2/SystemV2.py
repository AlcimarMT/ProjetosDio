menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""
__SALDO = 1000
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
operations = list()


def Deposit(num):
    if num >= 0:
        operations.append(num)
        
def Withdraw(num):
    if (num <= __SALDO) and (num <= limite):
        operations.append(-num)
        
def DepFunc():
    qtd = int(input("Informe o valor do depósito: R$"))
    global __SALDO
    if qtd >= 0:
        Deposit(qtd)
        __SALDO += qtd
    else:
        print("Valor não aceito.")

def SaqFunc():
    qtd = int(input("Informe o valor do saque: R$"))
    global __SALDO
    global numero_saques
    Withdraw(qtd)
    
    if ((qtd >= 0) and (qtd <= limite)) and ((__SALDO - qtd) >= 0) and (numero_saques < LIMITE_SAQUES):         
        __SALDO -= qtd
        numero_saques += 1
    else:
        if (qtd < 0):
            print("O valor inserido não é válido.")
        if (qtd > limite):
            print("O valor do saque excedeu o limite máximo.")
        if (numero_saques >= LIMITE_SAQUES):
            print("O número máximo de saques foi excedido.")
        if ((__SALDO - qtd) < 0):
            print("O saldo de", __SALDO, "não é suficiente para a quantidade a ser retirada.")
    

def ExtracFunc():
    print("===============Extrato===============")
    print(f"O saldo da sua conta é de: R$ {__SALDO:.2f}.")
    if len(operations) == 0:
        print("Nenhuma movimentação ocorreu nessa conta.")
    else:
        print("As seguites operações foram realizadas:\n")
        for i in operations:
            if i == 0:
                print("Nenhum valor foi subtraído ou adicionado à sua conta.")
            elif i < 0:
                print(f"Saque: R$ {-i:.2f}")
            else:
                print(f"Depósito: R$ {i:.2f}")
    print("=====================================")

def QuitFunc():
    print("Saindo da aplicação.")



while True:
    opcao = input(menu)
    
    if opcao == "d":
        DepFunc()
    elif opcao == "s":
        SaqFunc()
    elif opcao == "e":
        ExtracFunc()
    elif opcao == "q":
        QuitFunc()
        break
    else:
        print("Opção Inválida.")