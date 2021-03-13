import pickle
from repo.RepoError import RepositoryError



class GenericFileRepository:

    def __init__(self, filename):
        self.__storage = {}
        self.__filename = filename

    def __load_from_file(self):
        try:
            with open(self.__filename, 'rb') as f_read:
                self.__storage = pickle.load(f_read)
        except FileNotFoundError:
            self.__storage.clear()
        except Exception:
            self.__storage.clear()

    def __save_to_file(self):

        with open(self.__filename, 'wb') as f_write:
            pickle.dump(self.__storage, f_write)

    def creeaza(self, entity):
        '''
        creeaza o entitate
        :param entity: entitatea de creat
        :return: -
        '''
        self.__load_from_file()
        id_entity = entity.id_entity

        self.__storage[id_entity] = entity
        self.__save_to_file()

    def citeste(self, id_entity=None):
        '''
        da entitatile cerute
        :param id_entity: id(optional)
        :return: lista de entitati cerute sau entitatea cu id ul dat
        '''
        self.__load_from_file()
        if id_entity is None:
            return self.__storage.values()

        if id_entity in self.__storage:
            return self.__storage[id_entity]
        return None

    def modifica(self, entity):
        '''
        modifica o entitate
        :param entity: entitatea de modificat
        :return: -
        '''
        self.__load_from_file()
        id_entity = entity.id_entity
        if id_entity not in self.__storage:
            raise RepositoryError('Nu exista acest ID!')
        self.__storage[id_entity] = entity
        self.__save_to_file()

    def sterge(self, id_entity):
        '''
        sterge o entitate
        :param id_entity: id ul entitatii de modificat
        :return:
        '''
        self.__load_from_file()
        if id_entity not in self.__storage:
            raise RepositoryError('Nu exista acest ID!')
        del self.__storage[id_entity]
        self.__save_to_file()


    def goleste(self):
        self.__storage.clear()