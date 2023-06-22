__SALDO = 2000
withdraws = list()

def Withdraw(num):
    if num <= __SALDO:
        withdraws.append(num)
    if num < 0:
        print("Not possible.")

while True:
    opcao = int(input())
    if opcao == 1:
        qtd = int(input())
        Withdraw(qtd)
        if (qtd >= 0) and ((__SALDO - qtd) >= 0):
            __SALDO -= qtd
        else:
            print("O saldo de", __SALDO, " não é suficiente para a quantidade a ser retirada.")
    elif opcao == 2:
        for i in withdraws:
            print(i)
    else:
        print("saldo",__SALDO)
        break