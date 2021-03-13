from repo.RepoError import RepositoryError
from domain.medicament_vlidator import MedicamentError

class Console:
    def __init__(self,medicament_service):
        self.__medicament_service=medicament_service

    def __show_list(self,lista):
        for object in lista:
            print(object)

    def __show_menu(self):
        print('--Farmacie ONLINE--')
        print('1.Medicamente')
        print('x.Iesire')

    def run_console(self):
        while True:
            self.__show_menu()
            op=input('Alege optiunea: ')
            if op=='1':
                self.__meniu_medicamente()
            elif op=='x':
                break
            else:
                print('Comanda invalida!')

    def __show_meniu_medicamente(self):
        print('--Medicamente--')
        print('1. Adaugare')
        print('2. Stergere')
        print('3. Modifcare')
        print('a. Afisare medicamente')
        print('u. Undo')
        print('r. Redo')
        print('b. Back')


    def __handle_adaugare_med(self):
        try:
            nume=input('Dati numele medicamentului:')
            producator=input('Dati numele producatorului: ')
            pret=float(input('Dati pretul medicamentului: '))
            reteta=input('Este necesara reteta pentru acest medicament: ')
            self.__medicament_service.adaugare(nume,producator,pret,reteta)
            print('Adaugare efectuata!')
        except ValueError as ve:
            print('Date invalide ',ve)
        except RepositoryError as re:
            print(re)
        except MedicamentError as me:
            print(me)



    def __handle_stergere_med(self):
        try:
            id_med=int(input('Dati id-ul medicamentului de sters: '))
            self.__medicament_service.stergere(id_med)
            print('Stergere efectuata!')
        except ValueError as ve:
            print(ve)
        except RepositoryError as re:
            print(re)



    def __handle_modificare_med(self):
        try:
            id_med=int(input('Dati id ul medicamentului de modificat: '))
            nume=input('Dati noul nume(apasati ENTER pentru a nu schimba numele): ')
            producator=input('Dati numele producatorului(ENTER pentru a nu schimba nimic): ')
            pret=input('Dati pretul medicamentului(ENTER pentru a nu schimba nimic): ')
            reteta=input('Este necesara reteta?(ENTER pentru a nu schimba nimic): ')
            self.__medicament_service.modificare(id_med,nume,producator,pret,reteta)
            print('Medicament modificat!')
        except ValueError as ve:
            print('Date invalide!')
        except RepositoryError as re:
            print(re)
        except MedicamentError as me:
            print(me)



    def __handle_undo_med(self):
        if self.__medicament_service.undo()==1:
            print('Undo efectuat!')
        else:
            print('Nu se poate face undo!')


    def __handle_redo_med(self):
        if self.__medicament_service.redo()==1:
            print('Redo efectuat!')
        else:
            print('Nu se poate face redo!')





    def __meniu_medicamente(self):
        while True:
            self.__show_meniu_medicamente()
            op = input('Alegeti optiunea: ')
            if op=='1':
                self.__handle_adaugare_med()
            elif op=='2':
                self.__handle_stergere_med()
            elif op=='3':
                self.__handle_modificare_med()
            elif op=='a':
                self.__show_list(self.__medicament_service.get_all())
            elif op=='u':
                self.__handle_undo_med()
            elif op=='r':
                self.__handle_redo_med()
            elif op=='b':
                break
            else:
                print('Comanda invalida!')





