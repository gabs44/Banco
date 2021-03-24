from cliente import Cliente as C
from conta import Conta as CO

class Banco:
    def __init__(self, agencia):
        self.clientes = []
        self.contas = []
        self.agencia = agencia
    
    def add_cliente(self, cliente):
        if isinstance(cliente, C):
            self.clientes.append(cliente)
        else:
            print('erro')

    def add_conta(self, conta):
        if isinstance(conta, CO):
            self.contas.append(conta)
        else:
            print('erro')

    def get_agencia(self):
        return self.agencia

    def set_agencia(self, nova_agencia):
        self.agencia = nova_agencia

    def autenticacao(self, cliente, conta):
        if cliente.getconta() != conta:
            return False
        if isinstance(cliente, C) and isinstance(conta, CO):
            return (cliente in self.clientes and conta in self.contas and conta.agencia == self.agencia)      
        return False

    