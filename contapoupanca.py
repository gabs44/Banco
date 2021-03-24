from conta import Conta as P

class Poupanca(P):
    def __init__(self, agencia, num_conta, saldo):
        super().__init__(agencia, num_conta, saldo)


    def sacar(self, valor):
        if self.saldo < valor: 
            print('essa operação não pode ser realizada ')
        else:
            self.saldo -= valor
        self.dados()

    

