from domain.entity import Entity

class Medicament(Entity):
    def __init__(self,nume,producator,pret,reteta):
        super(Medicament, self).__init__()
        self.__nume=nume
        self.__producator=producator
        self.__pret=pret
        self.__reteta=reteta

    @property
    def nume(self):
        return self.__nume

    @property
    def producator(self):
        return self.__producator

    @property
    def pret(self):
        return self.__pret

    @property
    def reteta(self):
        return self.__reteta

    @reteta.setter
    def reteta(self,ret):
        self.__reteta=ret

    def __str__(self):
        return f' {self.id_entity}. Medicament: {self.nume} Producator: {self.producator},  {self.pret} RON, reteta: {self.reteta} '

    def __eq__(self, other):
        if type(self)!=type(other):
            return False
        return self.id_entity==other.id_entity




