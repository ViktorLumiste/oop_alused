from praks2.sodurid1 import Inimene


class Sodur(Inimene):
    def __init__(self, armee_nr):
        super().__init__()
        self.armee_nr = armee_nr

    def info(self):
        super().info()
