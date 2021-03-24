from conta import Conta as C

class ContaCorrente(C):
    def __init__(self, agencia, num_conta, saldo, limite=600):
        super().__init__(agencia, num_conta, saldo)
        self.__limite = limite


    @property
    def limite(self):
        return self.__limite


    def sacar(self, valor):
        if (self.saldo + self.__limite) < valor: 
            print('essa operação não pode ser realizada')
        else:
            self.saldo -= valor
        self.dados()
