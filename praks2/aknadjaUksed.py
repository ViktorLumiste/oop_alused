class AknadUksed:
    def __init__(self, pikkus, laius):
        self.pindala = pikkus * laius

class Tuba:
    def __init__(self, pikkus, laius, korgus):
        self.aknad_uksed = []
        self.pikkus = pikkus
        self.laius = laius
        self.korgus = korgus
        self.tap_rull = 0
    def pindalad(self, korgus, pikkus, laius):
        pind = 2 * korgus * (pikkus + laius)
        return pind
    def lisaAkenUks(self, laius, korgus):
        self.aknad_uksed.append(AknadUksed(laius, korgus))
    def tapp_rull(self, pikkus, laius):
        self.tap_rull = pikkus * laius
    def tooPind(self):
        uus_pindala = self.pindalad(self.korgus, self.pikkus, self.laius)
        for element in self.aknad_uksed:
            uus_pindala = uus_pindala - element.pindala
        self.tap_rull = uus_pindala / self.tap_rull
        print("{0} ruutmeetri jaoks kulub {1} tapeedi rulli".format(self.pindalad(self.korgus, self.pikkus, self.laius), round(self.tap_rull)))
        return uus_pindala