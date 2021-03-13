from domain.entity import Entity

class Card_client(Entity):
    def __init__(self,nume,prenume,CNP,data_nasterii,data_inregistrarii):
        super(Card_client, self).__init__()
        self.__nume = nume
        self.__prenume = prenume
        self.__CNP = CNP
        self.__data_nasterii = data_nasterii
        self.__data_inregistrarii = data_inregistrarii

    @property
    def nume(self):
        return self.__nume

    @property
    def prenume(self):
        return self.__prenume

    @property
    def CNP(self):
        return self.__CNP

    @property
    def data_nasterii(self):
        return datetime.datetime(
            int(self.__data_nasterii[6] + self.__data_nasterii[7] + self.__data_nasterii[8] + self.__data_nasterii[9]),
            int(self.__data_nasterii[3] + self.__data_nasterii[4]),
            int(self.__data_nasterii[0] + self.__data_nasterii[1]))

    @property
    def data_inregistrarii(self):
        return datetime.datetime(int(
            self.__data_inregistrarii[6] + self.__data_inregistrarii[7] + self.__data_inregistrarii[8] +
            self.__data_inregistrarii[9]), int(self.__data_inregistrarii[3] + self.__data_inregistrarii[4]),
                                 int(self.__data_inregistrarii[0] + self.__data_inregistrarii[1]))

    def __str__(self):
        return f'1.{self.nume} {self.prenume}, {self.CNP}, data nasterii: {self.data_nasterii}, data inregistarii: {self.data_inregistrarii}'

    def __eq__(self,other):
        if type(self)!=type(other):
            return False
        return self.id_entity==other.id_entity
