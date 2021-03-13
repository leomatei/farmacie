class MedicamentError(Exception):
    pass

class MedicamentValidator:
    def validare(med):
        errors=[]

        if med.reteta not in ['da','nu']:
            errors.append('Campul de reteta nu este introdus bine!')


        if errors!=[]:
            raise MedicamentError(errors)