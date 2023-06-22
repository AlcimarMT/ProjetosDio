class Cliente:
    def __init__(self,endereco):
        self.endereco= endereco
        self.contas = list()
        
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self,conta):
        self.contas.append(conta)
        
class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        
class ContaBanco:
    def __init__(self,numero,cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero,cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo        #acessou a propriedade do saldo. Essa linha existe para que a comparação seguinte seja possível.
        excedeu_saldo = valor > saldo
        
        if excedeu_saldo:
            print("O saque excedeu o valor do saldo disponível.")    

        elif valor > 0:
            self._saldo -= valor
            print("O saque foi realizado com sucesso.")
            return True
        else:
            print("O valor não é válido.")
        return False
    
    def depositar(self,valor):
        if valor > 0:
            self._valor += valor
            print("Depósito feito com sucesso.")
        else:
            print("Valor inválido.")
            return False

        return True
   
clientes=list()
contas = list()
numero_conta = len(contas)
cpf = str()

def filtrar_cliente(cpf,clientes):
    cliente=[cliente for cliente in clientes if clientes.cpf == cpf]
    return cliente[0]
def inputA():
    ans = input("Digite a opção:")
    return ans
    
while True:
    interator = inputA()
    if not cpf:
        cpf = input("Digite o CPF: ")
    elif (interator == "filtrar") and clientes:
        cliente = filtrar_cliente(cpf,clientes)
        print("Vazio" if not cliente else "Encontrou Algo")
    elif len(clientes) == 0:
        print("="*10,"Criando o Novo Cliente","="*10)
        print("="*30)
    elif inputA() == "J":
        break
    else:
        pass
def byPass():
    cpf = input("Informe o CPF do cliente novo: ")
    cliente = filtrar_cliente(cpf, clientes)
    if cliente:
        print("Já existe cliente com esse CPF.")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a sua data de nascimento: ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
        
    cliente = PessoaFisica(nome = nome, data_nascimento=data_nascimento, cpf = cpf, endereco = endereco)
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso.")