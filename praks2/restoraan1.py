class Restoraan():
    def __init__(self, r_nimi, s_tuup):
        self.res_nimi = r_nimi
        self.soog_tyyp = s_tuup
    def kirjelda_restoran(self):
        kirj_tekst = self.res_nimi + " pakub " + self.soog_tyyp
        print(kirj_tekst)

    def ava_restoraan(self):
        print(self.res_nimi + " on avatud")