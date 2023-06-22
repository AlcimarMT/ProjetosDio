from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime
import textwrap

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
 
def criar_cliente(clientes):
    cpf = input("Digite o CPF (valor de - para cancelar o loop): ")
    cliente = filtrar_clientes(cpf,clientes)
    if cliente:
        print("o CPF ja está vinculado a um cliente. ")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a sua data de nascimento: ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    
    cliente = PessoaFisica(nome = nome, data_nascimento=data_nascimento, cpf = cpf, endereco = endereco)
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso.")
    
while True:
    a = len(clientes)
    criar_cliente(clientes)
    if len(clientes) > a:
        print("Novo Cliente\n", clientes)