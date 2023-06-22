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

clientes = [PessoaFisica("Dave Jhones","05-01-1990","123","blecaute novembro"),PessoaFisica("Dave Jhones","05-01-1990","564","blecaute novembro"),PessoaFisica("Dave Jhones","05-01-1990","258","blecaute novembro")]
cpfs = ["123","159","753","258"]


def filtrar_cliente(cpf,clientess):
    clientex = [cliente for cliente in clientess if cliente.cpf == cpf]
    return clientex


for n in range(len(cpfs)):
    print(cpfs[n],["True" if filtrar_cliente(cpfs[n],clientes) else "False"][0])