class Kasutajad():
    def __init__(self, e_nimi, p_nimi,):
        self.eesnimi = e_nimi
        self.perekonnanimi = p_nimi

    def setandmed(self, age,mail):
        self.email = mail
        self.vanus = age

    def kirjelda_kasutaja(self):
        print("Kasutaja ees- ja perekonna nimi on:  {0} {1} ".format(self.eesnimi,self.perekonnanimi))
        print("Kasutaja email on : {0}" .format(self.email))
        print("Kasutaja vanus on :{0}".format(self.vanus))
    def tervita_kasutaja(self):
        print("Tere, {0} {1}".format(self.eesnimi, self.perekonnanimi))