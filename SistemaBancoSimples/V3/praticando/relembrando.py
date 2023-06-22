class Conta:
    def __init__(self,valor):
        self.__valor = valor
        
class ContaBancaria(Conta):
    def __init__(self, valor,names):
        super().__init__(valor)
        self.names=list()
    
    def __str__(self):
        return f"os nomes são: {self.names}"
    
    @property
    def name(self):
        return self.names
    
    def extend_names(self, moreNames):
        self.names.extend(moreNames)
        
def TreinandoClasses():   
    A = ContaBancaria(5,list())
    names2 = ["Murilo","Vitor","Joao","Euler"]

    print(A)
    A.extend_names(names2)
    print(A)



Brinquedos = {"bola":["azul"],"tamanho":["5"]}
extender = {"bola":["vermelho"],"tamanho":["2"]}
print(Brinquedos)
for keys1 in Brinquedos.keys():
    for keys2 in extender.keys():
        if keys1 == keys2:
            Brinquedos[keys1].extend(extender[keys2])

print(Brinquedos)
    
