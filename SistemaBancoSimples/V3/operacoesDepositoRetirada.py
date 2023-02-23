from oops import *


class deposito:
    @staticmethod
    def dep(cliente,quantia):
        antigoSaldo = cliente.retornarSaldo
        novoSaldo = antigoSaldo + quantia
        cliente.definirSaldo(novoSaldo)
        
class saque:
    @staticmethod
    def saq(cliente,quantia):
        antigoSaldo = cliente.retornarSaldo
        novoSaldo = antigoSaldo - quantia        
        cliente.definirSaldo(novoSaldo)
class operador:
    @staticmethod
    def operadorBanco(cliente,operacao:str,quantia):
        antigoSaldoCliente = cliente.retornarSaldo
        novoSaldoClienteSaque = antigoSaldoCliente - quantia
    
        if (type(cliente) == pessoaFisica) or (type(cliente)== pessoaJuridica):
            if not quantia < 0:
                if operacao == 'deposito':
                    deposito.dep(cliente,quantia)
                    cliente.his.atualizarHistorico(quantia=quantia,tipo="deposito")
                elif operacao == 'saque':
                    if novoSaldoClienteSaque >= 0:
                        saque.saq(cliente,quantia)
                        cliente.his.atualizarHistorico(quantia=quantia,tipo="saque")
                    else:
                        print("A quantia de saque é superior ao saldo disponível.")
                else:
                    print("operacao inválida.")
            else:
                print("A quantia deve ser um numero não negativo.")
        else:
            print("O cliente não foi definido")


    
