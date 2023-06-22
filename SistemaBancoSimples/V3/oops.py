from functionsPlayground import *
from functionsPlayground import random_code


class historicoOps:
    def __init__(self):
        self.historia = str()
    
    def atualizarHistorico(self,/,quantia,tipo):
        if type(quantia) == str:
            return "a quantia deve ser um número"
        if (type(tipo)==str) and (tipo == "saque" or tipo == "deposito"):
            self.historia += f"O {tipo} foi de {quantia}. \n"  
    def informarHistorico(self):
        return f"{self.historia}" if self.historia else "Nenhuma operação foi realizada."
    
class clientes:
    def __init__(self,nome):
        self.nome = nome
        self.saldo = 0
        self.num = random_code(16)
        self.his = historicoOps()

    @property
    def identificador(self):
        return self.nome
    
    @property
    def retornarSaldo(self):
        return self.saldo
    
    @property
    def retornarNum(self):
        return self.num
    @property
    def ImprimaOHistorico(self):
        return self.his.informarHistorico()
    
    def definirSaldo(self,quantia):
        if quantia >= 0:
            self.saldo = quantia

        else:
            print("A quantia não pode ser negativa.")

class pessoaFisica(clientes):
    def __init__(self,nome):
        super().__init__(nome)        
        self.tipo = "Pessoa Física"
        
class pessoaJuridica(clientes):
    def __init__(self,nome):
        super().__init__(nome)        
        self.tipo = "Pessoa Jurídica"
            
class registroClientes:
    def __init__(self):
        self.clientes = list()
        self.contas = list()
    
    @property
    def clientesCadastrados(self):
        return self.clientes
    
    @property
    def contasCadastradas(self):
        return self.contas
    
    @staticmethod
    def encontrarCliente(clientes,identificadorLista,nomeCliente):
        if (identificadorLista == 'clientes') or (identificadorLista == 'contas'):
            if identificadorLista == 'clientes':
                return [cliente for cliente in clientes.clientesCadastrados if cliente.identificador == nomeCliente]
            else:
                return [cliente for cliente in clientes.contasCadastradas if cliente.identificador == nomeCliente]
        else:
            print(f"Escolha um identificado viável dentre as disponíveis: clientes ou contas.")
            return
    def registrar_cliente(self,nome,tipo):
        clienteProcurado = registroClientes.encontrarCliente(self,'clientes',nome)
        if not clienteProcurado:
            if tipo == 'PJ':
                self.clientes.append(pessoaJuridica(nome))
            elif tipo == 'PF':
                self.clientes.append(pessoaFisica(nome))
            else:
                print("o tipo não é válido.")
        else:
            print("O cliente ja foi registrado anteriormente.")
            if not registroClientes.encontrarCliente(self,'contas',nome):
                print("O cliente não tem uma conta bancária conosco.")
            
    def registrar_contaBanco(self, nome):
        usuarioProcurado = registroClientes.encontrarCliente(self,'clientes',nome)
        if not usuarioProcurado:
            print("Registre o cliente na base de usuários primeiro.")
            return
        clienteProcurado = registroClientes.encontrarCliente(self,'contas',nome)
        if not clienteProcurado:
            self.contas.append(usuarioProcurado[0])
        else:
            print("O cliente já tem uma conta bancária cadastrada no sistema.")
            return      
    
    
    
    

