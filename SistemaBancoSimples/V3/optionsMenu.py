def criar_cliente(clientes):
    nomeCliente = input("informe o nome do usuário a ser cadastrado:")
    tipoCliente = input("O usuário é uma Pessoa Física (PF) ou uma Pessoa Jurídica (PJ)? Informe a sigla respectiva. ")
    respostas = ["PF","PJ"]
    while not tipoCliente in respostas:
        tipoCliente = input("Qual a sigla do tipo de clinte? PF ou PJ.") 
    clientes.registrar_cliente(nomeCliente, tipoCliente)
def criar_conta_bancaria(clientes):
    nomeCliente = input("informe o nome do usuário a ser cadastrado:")
    clientes.registrar_contaBanco(nomeCliente)

def listar_clientes_registrados(clientes):    
    listClientes = clientes.clientesCadastrados
    for cliente in listClientes:
        print(f"Nome: {cliente.identificador}, Tipo de Cliente: {cliente.tipo}, Registro: {cliente.retornarNum}")

def listar_contas_bancarias(clientes):
    listClientes = clientes.contasCadastradas
    for cliente in listClientes:
        print(f"Nome: {cliente.identificador}, Saldo: {cliente.retornarSaldo}")
