from animal import Animal
from interface_animal import InterfaceAnimal
from dono import Dono


class Gato(Animal, InterfaceAnimal):
    def __init__(self, nome, idade, cor, qnt_bolinhas, dono=Dono('')):
        super().__init__(nome, idade, cor)
        self.__qnt_bolinhas = qnt_bolinhas
        self.__dono = dono
        
    def __str__(self):
        return 'Dados dos gatos:'\
               f'\nNome: {self.nome}'\
               f'\nIdade: {self.idade}'\
               f'\nCor: {self.cor}'\
               f'\nQuantidade de bolinhas: {self.qnt_bolinhas}'\
               f'\nDono: {self.dono.nome}'      
        
    @property
    def qnt_bolinhas(self):
        return self.__qnt_bolinhas
    
    @qnt_bolinhas.setter
    def qnt_bolinhas(self, qnt_bolinhas):
        self.__qnt_bolinhas = qnt_bolinhas    
        
    @property
    def dono(self):
        return self.__dono
    
    @dono.setter
    def dono(self, dono):
        self.__dono = dono
        
    def fazer_barulho(self):
        return 'miau'  
    
    def brincar(self):
        self.felicidade += 1
        return 'Gato está brincando'