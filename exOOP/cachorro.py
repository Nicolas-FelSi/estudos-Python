from animal import Animal
from interface_animal import InterfaceAnimal
from dono import Dono


class Cachorro(Animal, InterfaceAnimal):
    def __init__(self, nome, idade, cor, qnt_brinquedos, dono=Dono('')):
        super().__init__(nome, idade, cor)
        self.__qnt_brinquedos = qnt_brinquedos
        self.__dono = dono

    def __str__(self):
        return 'Dados dos cachorros:'\
               f'\nNome: {self.nome}'\
               f'\nIdade: {self.idade}'\
               f'\nCor: {self.cor}'\
               f'\nQuantidade de brinquedos: {self.qnt_brinquedos}'\
               f'\nDono: {self.dono.nome}'                

    @property
    def qnt_brinquedos(self):
        return self.__qnt_brinquedos

    @qnt_brinquedos.setter
    def qnt_brinquedos(self, qnt_brinquedo):
        self.__qnt_brinquedos = qnt_brinquedo

    @property
    def dono(self):
        return self.__dono

    @dono.setter
    def dono(self, dono):
        self.__dono = dono

    def fazer_barulho(self):
        return 'au au'

    def brincar(self):
        self.felicidade += 2
        return 'Cachorro está brincando'
    
    
