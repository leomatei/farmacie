class CardError(Exception):
    pass

class CardValidator:
    def validare(card):
        errors = []
        if not (999999999999 < card.CNP and card.CNP < 10000000000000):
            errors.append('CNP-ul nu este valid')
