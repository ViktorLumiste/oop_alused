class Konto():
    def __init__(self, nimi, saldo):
        self.__nimi = nimi
        self.__saldo = saldo
    def deposiit(self, kogus):
        if kogus > 0:
            self.__saldo += kogus
        else:
            print("sisestage positiivne summa!")
    def ylekanne(self, amount):
        if amount > 0:
            self.__saldo -= amount
        else:
            print("sisestage positiivne summa!")
    def naita_saldo(self):
        return self.__saldo
    def naita_nimi(self):
        return self.__nimi