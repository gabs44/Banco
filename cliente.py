from pessoa import Pessoa as P

class Cliente(P):
    def __init__(self, nome, idade, conta):
        super().__init__(nome, idade)
        self.__conta = conta


    # get

    def getconta(self):
        return self.__conta

    # set

    def setconta(self, nova_conta):
        self.__conta = nova_conta


