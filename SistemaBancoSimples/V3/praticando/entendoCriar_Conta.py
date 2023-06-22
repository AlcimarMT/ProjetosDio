from abc import ABC, abstractclassmethod, abstractproperty

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass
    @abstractproperty
    def registrar(self,conta):
        pass

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


clientes = [PessoaFisica("Dave Jhones","05-01-1990","123","blecaute novembro")]

def filtrar_clientes(cpf, clientess):
    clientex = [cliente for cliente in clientess if cliente.cpf == cpf]
    return clientex

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("Cliente não possui conta.")
        return

    return cliente.contas[0]
