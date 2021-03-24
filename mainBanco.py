from cliente import Cliente as C
from contacorrente import ContaCorrente as CC
from contapoupanca import Poupanca as P
from banco import Banco as B


banco = B(13)

CC1 = CC(13, 5723568970, 500)
CC2 = CC(13, 9753323468, 1200)
CC3 = CC(13, 7909678897, 850)
CC4 = CC(13, 2345678002, 2000)

P1 = P(13, 8759057889, 460)
P2 = P(13, 4563780904, 220)
P3 = P(13, 3245678790, 900)
P4 = P(13, 2135465768, 150)

C1 = C('joão', 35, CC1)
C2 = C('Camilla', 28, CC2)
C3 = C('Gabriella', 18, P1)
C4 = C('Andressa', 18, P2)
C5 = C('Maria', 27, CC3 )
C6 = C('Eduarda', 19, CC4 )
C7 = C('Vitória', 23, P3)
C8 = C('Isabella', 39, P4)


banco.add_conta(CC1)
banco.add_conta(CC2)
banco.add_conta(CC3)
banco.add_conta(CC4)
banco.add_conta(P1)
banco.add_conta(P2)
banco.add_conta(P3)
banco.add_conta(P4)

banco.add_cliente(C1)
banco.add_cliente(C2)
banco.add_cliente(C3)
banco.add_cliente(C4)
banco.add_cliente(C5)
banco.add_cliente(C6)
banco.add_cliente(C7)
banco.add_cliente(C8)

def sacar(cliente, conta, valor):
    if banco.autenticacao(cliente,conta):
        print(f'seu saldo era de {conta.saldo} reais')
        conta.sacar(valor)

def depositar(cliente, conta, valor):
    if banco.autenticacao(cliente,conta):
        print(f'seu saldo era de {conta.saldo} reais')
        conta.depositar(valor)

print('Saques:')

sacar(C1, CC1, 120)
sacar(C3, P1, 20)
sacar(C2, CC2, 78)
sacar(C4, P2, 100)
sacar(C7, P3, 950)

print('Depósitos:')

depositar(C5, CC3, 550)
depositar(C8, P4, 200)
depositar(C6, CC4, 700)