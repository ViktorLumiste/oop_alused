class Restoraan():
    def __init__(self, r_nimi, s_tuup):
        self.res_nimi = r_nimi
        self.soog_tyyp = s_tuup
    teen_kyl = 0
    def kirjelda_restoran(self):
        kirj_tekst = self.res_nimi + " pakub " + self.soog_tyyp
        print(kirj_tekst)
    def maara_teenindatud_kyl(self, kyl_arv):
        self.teen_kyl = kyl_arv
    def suurenda_teen_kyl(self, suur_kyl_arv):
        self.teen_kyl += suur_kyl_arv

    def ava_restoraan(self):
        print(self.res_nimi + " on avatud")