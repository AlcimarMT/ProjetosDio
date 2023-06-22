from oops import*

import random, json, os


def Test_ClasseHistorico(listaTeste):
    depositosBanco = historicoOps()
    for keys in listaTeste:
        depositosBanco.atualizarHistorico(quantia=keys[1],tipo=keys[0])
    
    return depositosBanco.historia

#print(Test_ClasseHistorico(colecaoDeListas("operacoes")))


def Test_RegistroNewAccounts(clientes,outputtype = "registro"):
    
    for nome in ['nomes','empresas']:  
        clienteslista = colecaoDeListas(nome)
        for clientez in clienteslista:
            if nome == 'nomes':
                tipo = 'PF'
                clientes.registrar_cliente(clientez[0],tipo)
            elif nome == 'empresas':
                tipo = 'PJ'
                clientes.registrar_cliente(clientez[0],tipo)
    if outputtype == "registro":
        return clientes 
    else:
        return [clientes, clientes.clientesCadastrados] 
    
def Test_ImprimaOsHistorico(clientes):
    clientes = Test_RegistroNewAccounts(clientes, outputtype="historico")
    listaHistoricos = clientes[1]
    for client in listaHistoricos:
        print(client.ImprimaOHistorico)


def listarOpcoes(menu):
    menuOptions = re.findall('\[(.*?)\]',menu)
    menuDescriptions = re.findall('[A-Z].*?[\.]',menu)
    menuDicts = dict(zip(menuOptions,menuDescriptions))
    return menuDicts


def random_code(length):
    code = ""
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    for i in range(length):
        code += random.choice(characters)
    return code

def colecaoDeListas(selec = None):
    operacoes = [('Deposito', 1200), ('Saque', 500), ('Saque', 200), ('Deposito', 500),('Saque',1000)]
    nomes = [('John', 'A123'), ('Mary', 'B456'), ('Bob', 'C789'), ('Alice', 'D012')]
    empresas = [('Apple', 'A-12345'), ('Google', 'G-54321'), ('Microsoft', 'M-98765'), ('Amazon', 'A-67890')]
    
    
    nomes_vars = ["operacoes","nomes","empresas"]
    Listas = dict(zip(nomes_vars,[operacoes,nomes,empresas]))
    
    if selec in Listas:
        return Listas[selec]
    else:
        print(f"Informe uma das opções válidas:{nomes_vars}")
        return ""


def Test_Operacoes(clientesLista):
    for clientes in clientesLista:
        clientes.definirSaldo(random.randint(200,500))
    
def testeComClientes(clientes):
    clientes, clientesRegistrados = Test_RegistroNewAccounts(clientes, outputtype = str())
    for cliente in clientesRegistrados:
        quantia = float(random.randint(200,500))
       
        operacoesDepositoRetirada.operador.operadorBanco(cliente,random.choice(["deposito","saque"]),quantia = quantia)
        print(cliente.ImprimaOHistorico)
    clientesRegistradosResume = [[cliente.identificador,cliente.retornarSaldo,f"pessoaFisica: {type(cliente)==pessoaFisica}",f"pessoaJuridica: {type(cliente)==pessoaJuridica}"] for cliente in clientesRegistrados]
    

def testFiltroCliente(clientes):
    clientes, clientesRegistrados = Test_RegistroNewAccounts(clientes, outputtype = str())
    nomes = list()
    for name in clientesRegistrados:
        name = name.identificador
        nomes.append(name)
    nomes[2] = "Rita"
    nomes[6] = "Fiat"
    listaFiltrada = list()
    for name in nomes:
        varA = registroClientes.encontrarCliente(clientes, 'clientes', name)
        listaFiltrada.append(varA)
    print(listaFiltrada)

def passWord(fileName,/,passLength = 10, reNew=False):
    fileName = fileName + ".txt"
    def newPassword(fileName):
        with open(fileName,"w") as file:
            password = str()
            for _ in range(passLength):
                char = 'abcdefghijklmnopqrstuvxz1234567890'
                password = password + random.choice(char)
            file.write(password)
    
    def conteudoPassword(fileName):
        with open(fileName,"r") as file:
            connteudofile = file.read()
            print(connteudofile)
    currentDir = str(os.getcwd())
    currentFile = currentDir + "\\" + fileName
    estadoArquivo = os.path.isfile(currentFile)
    if not estadoArquivo:
        newPassword(fileName)
        return
    if not reNew:
        with open(fileName,"r") as file:
            filecontent = file.read()
            if not filecontent:
                newPassword(fileName)
            else:
                print(f"O arquivo já tem uma senha. {filecontent}")
        
    if reNew:          
        newPassword(fileName)        
        print("Uma nova senha foi criada.")
    
