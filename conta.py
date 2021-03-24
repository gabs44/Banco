from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, num_conta, saldo):
        self.__agencia = agencia
        self.__num_conta = num_conta
        self.__saldo = saldo

    # getters
    # Usando encapsulamento para manter a segurança dos dados

    @property
    def agencia(self):
        return self.__agencia

    @property
    def num_conta(self):
        return self.__num_conta

    @property
    def saldo(self):
        return self.__saldo

    # set

    @saldo.setter
    def saldo(self, valor):
        if (type(valor) == type(int())) or (type(valor) == type(float()))  :
            self.__saldo = valor 
        else:
            print('erro')


    def depositar(self, valor):
        if (type(valor) == type(int())) or (type(valor) == type(float()))  :
            self.__saldo += valor
        self.dados()

    def dados(self):
        print(f'Sua agência é a {self.agencia}')
        print(f'O número da sua conta é {self.num_conta}')
        print(f'O seu saldo atual é de {self.saldo} reais')


    @abstractmethod
    def sacar(self):
        pass


