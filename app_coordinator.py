from domain.medicament_vlidator import MedicamentValidator
from repo.GenericRepo import GenericFileRepository
from service.MedicamentService import MedicamentService
from user_interface.console import Console

med_repo=GenericFileRepository('medicamente.pkl')

med_validator=MedicamentValidator

med_serv=MedicamentService(med_repo,med_validator)

console=Console(med_serv)
console.run_console()