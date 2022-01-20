class Inimene():
    def __init__(self, enimi, pnimi, kutse_kval = 1):
        self.enimi = enimi
        self.pnimi = pnimi
        self.kutse_kval = kutse_kval
    def tutvustus(self):
        print("Tere, olen,", self.enimi,self.pnimi)
    def __del__(self):
        print("Kõige head")