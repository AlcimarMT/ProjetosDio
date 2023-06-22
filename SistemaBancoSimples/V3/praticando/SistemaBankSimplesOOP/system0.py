class Bank:
    name = "Banco Danonez"
    contas = list()
    
    
    def update_db(self,conta):
        self.contas.append(conta)
        
    def autenticar(self,name,numero_conta):
        for i in range(len(self.contas)):
            if name in self.contas[i].name and numero_conta in self.contas[i].nconta:   
                return self.contas[i].name
            else:
                return    

class Account:
    def __init__(self,name,nconta):
        self.name = name
        self.nconta = nconta
        self.balance = 0
        
    def depositar(self,value):
        if value > 0:
            self.balance += value
        else: 
            return "A operação não é possível."
    def retirada(self,value):
        if value > 0 and value + self.balance >= 0
            self.balance -= value
        else:
            return "A operação não é possível."
    
    def balance(self):
        print(f"Balance is:{self.balance}")    
        
while True:
    name = input("Digite o Nome: ")
    numero_conta = "0001"
    p = Account(name,numero_conta)
    sys = Bank()
    if sys.autenticar(p.name,p.nconta):
        listaContas = [contas.name for contas in sys.contas]
        print(listaContas)
        break
    else:
        sys.update_db(p)