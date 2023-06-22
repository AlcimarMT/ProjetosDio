from oops import *
from functionsPlayground import *
from optionsMenu import criar_cliente, criar_conta_bancaria, listar_clientes_registrados, listar_contas_bancarias
from operacoesDepositoRetirada import operador

menuCliente = """
[nome]     - Informe o nome do cliente.
[q]        - Sair.

Opção:
"""

menuNormal = """
[deposito] - Depósito de uma quantia na conta do cliente.
[saque]    - Saque uma quantia inferior ou igual ao saldo de sua conta.
[extrato]  - Imprimir todas as operações realizadas por um titular.
[dados]    - Imprimir os dados do presente usuário.
[q]        - Sair do contexto.

Opção: 
"""
opcoesNormal = ["deposito","saque","extrato","dados","q"]

menuADM = """
[ccl] - Criar cliente.
[ccb] - Criar conta bancária.
[lcl] - Listar clientes registrados.
[lcb] - Listar contas bancárias.

Opção: 
"""
opcoesADM = ["ccl","ccb","lcl","lcb","normal"]

clientes = registroClientes()
clientes.registrar_cliente("Jhon","PF")
clientes.registrar_contaBanco("Jhon")

accessoADM = False

while True:
    if not accessoADM:
        input1 = input(menuCliente)
        if input1 == "normal":
            print("O contexto já está no campo de pesquisa de clientes.")
            continue
        if input1 == "q":
            break
        elif input1 == "adm":
            accessoADM = True
        else:
            contaPesquisada = clientes.encontrarCliente(clientes,'contas',input1)
            clientePesquisado = clientes.encontrarCliente(clientes,'clientes',input1)
            if not contaPesquisada:
                print("O cliente não está registrado na base de contas bancárias.")
                if not clientePesquisado:
                    print("O cliente também não está registrado na base de usuário.")
            else:
                cliente = contaPesquisada[0]
                
                while True:
                    input3 = input(menuNormal)
                    validacaoInput3 = input3 in opcoesNormal
                    if not validacaoInput3:
                        print("A opção não é válida.")
                    elif input3 == "q":
                        print("Saindo do presente contexto.")
                        break
                    elif input3 == "deposito":
                        input4 = input("O quanto deseja depositar? ")
                        input4 = float(input4)
                        operador.operadorBanco(cliente,"deposito", input4)
                    elif input3 == "saque":
                        if cliente.retornarSaldo == 0:
                            print("Não há saldo suficiente.")
                        else:
                            input4 = input("O quanto deseja sacar? ")
                            input4 = float(input4)
                            operador.operadorBanco(cliente,"saque", input4)
                    elif input3 == "extrato":
                        print(cliente.his.informarHistorico())
                    elif input3 == "dados":
                        print(f"{cliente.identificador}, {cliente.tipo}, Senha:{cliente.retornarNum}, Sald:{cliente.retornarSaldo}")
               
    else:
        while True:
            input2 = input(menuADM)
            validacaoInput = input2 in opcoesADM
                        
            if input2 == "normal":
                accessoADM = False
                break
            elif not validacaoInput:
                print("A opção não é válida.")
            elif input2 == "ccl":
                criar_cliente(clientes)
            elif input2 == "ccb":
                criar_conta_bancaria(clientes)
            elif input2 == "lcl":
                listar_clientes_registrados(clientes)
            elif input2 == "lcb":
                listar_contas_bancarias(clientes)
            
            
            
            
            
            
        

