'''

class Pessoa:
    def __init__ (self, nome, idade, cidade): 
        self.nome = nome
        self.idade = idade
        self.cidade = cidade

    def saudacao(self): 
        return f"Olá, eu sou {self.nome}, tenho {self.idade} anos e venho de {self.cidade}"

pessoa1 = Pessoa("Davi", 18, "Londrina")
print(pessoa1.saudacao())


class Carro: 
    def __init__(self, modelo, ano, marca):
        self.modelo = modelo
        self.ano = ano
        self.marca = marca

    def saudacao1(self):
        return f"Olá, temos um {self.modelo}, {self.ano} da marca {self.marca}, teria interesse?"

carro1 = Carro("911", 2023, "Porsche")
print(carro1.saudacao1())

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def som(self):
        pass

class Cachorro(Animal):
    def som(self):
        return f"{self.nome}, Au Au!!"

class Gato(Animal):
    def som(self):
        return f"{self.nome}, Miau!!"

__rex__ = Cachorro("Rex")
print(__rex__.som())

__snowball__ = Gato("Snow Ball")
print(__snowball__.som())
'''

