from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime
import textwrap

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
   
class ContaCorrente(ContaBanco):
    def __init__(self,numero,cliente, limite = 500, limite_saques=3):
        super().__init__(numero,cliente)
        self.limite = limite
        self.limite_saques= limite_saques
    
    def sacar(self,valor):
        numeros_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"]== Saque.__name__])
        excedeu_limite = valor > self.limite
        excedeu_saques = numeros_saques >= self.limite_saques
        
        if excedeu_limite:
            print("Operação falhou. O valor do saque excede o limite.")
        
        elif excedeu_saques:
            print("O número de saques foi excedido.")
            
        else:
            return super().sacar(valor)
    
        return False
    
    def __str__(self):
        return f"""
            Agência:   {self.agencia}
                C/C:   {self.numero}
            Titular:   {self.cliente.nome}    
    """

class Historico:
    def __init__(self):
        self._transacoes = []
        
    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self,transacao):
        self._transacoes["tipo"].append(transacao.__class__.__name__)
        self._transacoes["valor"].append(transacao.valor)
        self._transacoes["data"].append(datetime.now().strftime("%d-%m-%Y %H:%M:%s"))

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass
    @abstractproperty
    def registrar(self,conta):
        pass

class Deposito(Transacao):                           
    def __init__(self, valor):
        self._valor = valor
        
    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_trasacao = conta.depositar(self.valor)
        
        if sucesso_trasacao:
            conta.historico.adicionar_transacao(self)

class Saque(Transacao):                            
    def __init__(self, valor):
        self._valor = valor
        
    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_trasacao = conta.sacar(self.valor)
        
        if sucesso_trasacao:
            conta.historico.adicionar_transacao(self)    


def menu():
    menu = """\n
    ========================MENU========================
    [d]  Depositar
    [s]  Sacar
    [e]  Extrato
    [nu] Novo Usuário
    [nc] Nova Conta Bancária
    [lc] Listar Contas
    [q]  Sair
    """        
    return input(textwrap.dedent(menu))

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("Cliente não possui conta.")
        return

    return cliente.contas[0]

def depositar(clientes):
    cpf = input("Informar o CPF do cliente:")
    cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print("Cliente Não Encontrado")
        return
    
    valor = float(input("Informe o valor a ser depositado: "))
    transacao = Deposito(valor)
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return 
    
    cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
    cpf = input("Informar o CPF do cliente:")
    cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print("Cliente Não Encontrado")
        return
    
    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        print("O cliente naõ tem uma conta.")
        return 
    
    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    cpf = input("Informe o cpf do cliente: ")
    cliente = filtrar_cliente(cpf,clientes)
    
    if not cliente:
        print("Cliente não encontrado.")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    print("\n==============Extrato==============")    
    transacoes = conta.historico.transacoes
    
    extrato = ""
    
    if not transacoes:
        extrato = "Não foram realizadas transações nenhumas."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n  R$  {transacao['valor']:.2f}"
            
    print(extrato)
    print(f"\nSaldo:\n  R${conta.saldo:.2f}")
    print("==============Extrato==============")
    
def criar_cliente(clientes):
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
        
def criar_conta(numero_conta,clientes,contas):
    cpf = input("Informe o CPF do cliente novo: ")
    cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print("Cliente não encontrado, criação de conta errado.")
        return
    conta = ContaBanco.nova_conta(cliente=cliente,numero = numero_conta)
    contas.append(conta)


def listar_contas(contas,clientes):
    cpf = input("Informe o CPF do cliente novo: ")
    cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        return "Nenhum cliente com esse cpf foi encontrado."
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return "Nenhuma conta cadastrada."
    
    for conta in contas:
        print("="*100)
        print(textwrap.dedent(str(conta)))



def main():
    clientes = []
    contas = []
    
    while True:
        opcao = menu()
        
        if opcao == "d":
            depositar(clientes)
        
        elif opcao == "s":
            sacar(clientes)    
            
        elif opcao == "e":
            exibir_extrato(clientes)
            
        elif opcao == "nu":
            criar_cliente(clientes)
        
        elif opcao == "nc":
            numero_conta = len(contas)
            criar_conta(numero_conta, clientes, contas)
            
        elif opcao == "lc":
            listar_contas(contas,clientes)
        
        elif opcao == "q":
            break
        else:
            print("Operação inválida. Escolha uma opção dentre as do menu.")
            
            
main()
            