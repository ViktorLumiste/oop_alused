class Kasutajad():
    eesnimi = ""
    perekonnanimi = ""
    email = ""
    vanus = ""

    def setandmed(self, nimi,pnimi, age,mail):
        self.eesnimi = nimi
        self.email = mail
        self.perekonnanimi = pnimi
        self.vanus = age

    def kirjelda_kasutaja(self):
        print("Kasutaja ees- ja perekonna nimi on:  {0} {1} ".format(self.eesnimi,self.perekonnanimi))
        print("Kasutaja email on : {0}" .format(self.email))
        print("Kasutaja vanus on :{0}".format(self.vanus))
    def tervita_kasutaja(self):
        print("Tere, {0} {1}".format(self.eesnimi, self.perekonnanimi))

