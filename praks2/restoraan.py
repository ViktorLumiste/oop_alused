class Restoraan():
    restorani_nimi = ""
    soogi_tyyp = ""

    def kirjelda_restoran(self):
        kirj_tekst = self.restorani_nimi + " pakub " + self.soogi_tyyp
        print(kirj_tekst)

    def ava_restoraan(self):
        print(self.restorani_nimi + " on avatud")
