class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade 
    
def get_nome(self):
    return self.nome

def get_idade(self):
    return self.idade

def set_idade(self, pessoa_idade):
    if pessoa_idade >=0:
        self.idade = pessoa_idade
    else:
        print('valor negativo inserido')