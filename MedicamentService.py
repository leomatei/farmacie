from repo.GenericRepo import GenericFileRepository
from domain.medicament import Medicament

class MedicamentService:
    def __init__(self,repository,validator):
        self.__repo=repository
        self.__vali=validator
        self.__undo_op=[]
        self.__redo_op=[]

    def adaugare(self,nume,producator,pret,reteta):
        med=Medicament(nume,producator,pret,reteta)
        med.id_entity=self.id_count
        self.__vali.validare(med)
        self.__repo.creeaza(med)
        self.__undo_op.append(lambda : self.__repo.sterge(med.id_entity))
        self.__redo_op.append(lambda : self.__repo.creeaza(med))

    def stergere(self,id_med):
        med=self.__repo.citeste(id_med)
        self.__repo.sterge(id_med)
        for medicament in self.__repo.citeste():
            if medicament.id_entity<id_med:
                medicament.id_entity=medicament.id_entity-1
        self.__undo_op.append(lambda : self.__repo.creeaza(med))
        self.__redo_op.append( lambda : self.__repo.sterge(id_med))

    def modificare(self,id_med,nume,producator,pret,reteta):
        med_de_modificat=self.__repo.citeste(id_med)
        if nume=='':
            nume=med_de_modificat.nume
        if producator=='':
            producator=med_de_modificat.producator
        if pret=='':
            pret=med_de_modificat.pret
        else:
            pret=float(pret)
        if reteta=='':
            reteta=med_de_modificat.reteta
        med=Medicament(nume,producator,pret,reteta)

        med.id_entity=med_de_modificat.id_entity
        self.__vali.validare(med)
        self.__repo.modifica(med)
        self.__undo_op.append(lambda : self.__repo.modifica(med_de_modificat))
        self.__redo_op.append( lambda : self.__repo.modifica(med))


    def undo(self):
        if len(self.__undo_op)>0:
            undo_op=self.__undo_op.pop()
            undo_op()
            return 1
        return 0

    def redo(self):
        if len(self.__redo_op) > 0:
            redo_op = self.__redo_op.pop(0)
            redo_op()
            return 1
        return 0

    def get_all(self):
        return self.__repo.citeste()

    @property
    def id_count(self):
        return len(self.__repo.citeste())+1