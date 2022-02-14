from praks2.raamat import Raamat


class Raamatupood:
    def __init__(self, nimi, reiting):
        self.nimi = nimi
        self.reiting = reiting
    raamatud = []
    populaar = []

    def saan_lisada_raamat(self, raamat):
        for i in self.raamatud:
            if i.pealkiri == raamat.pealkiri and i.autor == raamat.autor:
                return False
            else:
                if raamat.reiting >= self.reiting:
                    return True
                else:
                    pass
        return True

    def lisa_raamat(self, raamat):
        if self.saan_lisada_raamat(raamat):
            self.raamatud.append(raamat)
            print("Raamat oli lisatud")
        elif not self.saan_lisada_raamat(raamat):
            print("Raamat ei saa lisada")
        else:
            print("Viga")

    def saan_eemaldada_raamat(self, raamat):
        for i in self.raamatud:
            if raamat.pealkiri == i.pealkiri and raamat.autor == i.autor:
                return True
            else:
                return False

    def eemalda_raamat(self, raamat):
        if self.saan_eemaldada_raamat(raamat):
            self.raamatud.remove(raamat)
            print("Raamat eemaldatud")
        else:
            print("Seda raamatut ei saa eemaldada")

    def naita_koik_raamatud(self):
        raa = []
        for i in self.raamatud:
            raa.append(i.pealkiri)
        print(raa)


    def naita_raamatud_hinna_jargi(self, ramaatud):
        hindSorted = sorted(ramaatud, key=lambda x: x.hind)
        print(hindSorted)

    def naita_koige_populaarsem_raamat(self, ramaatud):
        reitingSorted = sorted(ramaatud, key=lambda  x: x.reiting)
        print(reitingSorted[-1])


raamat1 = Raamat("1", 2, 6, 4)
raamat2 = Raamat("2", 3, 4, 5)
raamat3 = Raamat("2", 3, 4, 1)
raamatupood1 = Raamatupood("raamatupood1", 2)

raamatupood1.lisa_raamat(raamat1)
raamatupood1.lisa_raamat(raamat2)
raamatupood1.lisa_raamat(raamat3)
raamatupood1.naita_koik_raamatud()
raamatupood1.naita_raamatud_hinna_jargi(raamatupood1.raamatud)
raamatupood1.naita_koige_populaarsem_raamat(raamatupood1.raamatud)