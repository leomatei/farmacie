from repo.GenericRepo import GenericFileRepository
from domain.card_client import Card_client

class CardService:
    def __init__(self,repository,validator):
        self.__repository=repository
        self.__validator=validator
        self.__undo_op=[]
        self.__redo_op=[]

    @property
    def id_count(self):
        return len(self.__repository.citeste()) + 1

    def adaugare(self,nume,prenume,CNP,data_nasterii,data_inregistrarii):
        card=Card_client(nume,prenume,CNP,data_nasterii,data_inregistrarii)
        card.id_entity=self.id_count
        
