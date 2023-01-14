menu = """
[d]  Depositar
[s]  Sacar
[e]  Extrato
[nu] Novo Usuário
[nc] Nova Conta Bancária
[ls] Listar Contas
[q]  Sair

"""
__SALDO = 1000
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
operations = list()
usuarios = {"nome":["Jhon"],"data_nascimento":["05-02-1998"],"cpf":["123"], "endereco":["aaa"]}
cadastros = {"cpf":["123"],"agencia":["564879498-9"],"nconta":["5648794985656589"]}

def Depositar(saldo,valor,extrato):
    if valor > 0:
        saldo += valor 
        extrato += f"Deposíto:\t\tR$ {valor:.2f}\n"
    else:
        print("O valor não é válido.")
    return saldo, extrato

def Sacar(*, saldo,valor,extrato,limite,numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saques >= limite_saques
    
    if excedeu_saldo:
        print("Operação Falhou! Você não tem saldo suficiente para realizar esta operação.")
    elif excedeu_limite:
        print(f"Operação Falhou! O valor do saque excedeu o limite de {LIMITE_SAQUES}:.2f")
    elif excedeu_saque:
        print("Operação Falhou! O número máximo de saques foi excedido.")
    elif valor > 0:
        saldo -= valor
        extrato = f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n Saque realizado com sucesso.")
    
    else:
        print("Operação Falhou! O valor informado é inválido.")
        
    return saldo, extrato

def Exibir_extrato(saldo,/,*, extrato):
    print("===============Extrato===============")
    print("Não foram realizadas movimentações." if not extrato else extrato) #Se extrato n tiver conteudo nenhum, n será imprimido.
    print(f"O saldo da sua conta é de: R$ {__SALDO:.2f}.")
    print("=====================================")

def CriarUser(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = FiltrarUsers(cpf, usuarios)
    
    if usuario:
        print("Já existe um usuário com esse CPF.")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informa a sua data de nascimento (dd-mm-aa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    return {"nome":nome,"data_nascimento":data_nascimento,"cpf":cpf, "endereco":endereco}
    
    print("Usuário cadastrado com sucesso.")
       
def CriarConta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = FiltrarUsers(cpf,usuarios)
    
    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia":agencia,"nconta":nconta,"usuario":usuario}
    
    print("Usuário não cadastrado. Nenhuma conta foi criada.")    
    
def FiltrarUsers(cpf, usuarios):
    usuario_filtrados = [usuario for usuario in usuarios["cpf"] if usuario == cpf]
    return usuario_filtrados if usuario_filtrados else None

def ListarContas(contas):
    n = 0
    numeroContas = len(contas["nconta"])
    while n < numeroContas:
        resumeInfo = str()
        resumeInfo += "=================Resumo das contas=================\n"
        for key in contas:
            if key != 'cpf':
                resumeInfo+="    "
            resumeInfo += f"{key}:{contas[key][n]}"
            if key == "nconta":
                resumeInfo += "\n"
        
        n += 1
    resumeInfo += "===================================================\n"
    return resumeInfo

def Deposit(num):
    if num >= 0:
        operations.append(num)
def Withdraw(num):
    if (num <= __SALDO) and (num <= limite):
        operations.append(-num)

while True:
    opcao = input(menu)
    
    if opcao == "d":
        qtd = float(input("Informe o valor do depósito: R$"))
        saldo, extrato = Depositar(saldo, qtd, extrato)
    elif opcao == "s":
        qtd = int(input("Informe o valor do saque: R$"))
        saldo, extrato = Sacar(
            saldo = saldo,
            valor = qtd,
            extrato = extrato,
            limite = limite,
            numero_saques= numero_saques,
            limite_saques=LIMITE_SAQUES)
        
    elif opcao == "e":
        Exibir_extrato(saldo, extrato=extrato)
    elif opcao == "nu":
        temp = CriarUser(usuarios)
        if temp:
            for key in usuarios:
                usuarios[key].append(temp[key])
    elif opcao == "nc":
        agencia, nconta = str(),str()
        temp = CriarConta(agencia,nconta,usuarios)
        if temp:
            for key in usuarios:
                cadastros[key].append(temp[key])     
    elif opcao == "ls":
        listaDeContas = ListarContas(cadastros)
        print(listaDeContas)
    elif opcao == "q":
        print("Saindo da aplicação.")
        break
    else:
        print("Opção Inválida.")