#impordime tähtsad moodulid
from random import randint
from time import sleep
#Loome klassid
class Andmed:
    """Andmete hoidmise klass"""
    def __init__(self, *info):
        self.info = list(info)
    def __getitem__(self, i):
        return self.info[i]

class Opetaja:
    """Õpetaja klass õpetab õpilastele andmeid"""
    def opetab(self, info, *opilane):
        """Õpetab info õpilastele, vajab õpetatava info ja õpilaste nimed"""
        for i in opilane:
            i.opib(info)

class Opilane:
    """Õpilanse klass, hoiab õpitud teadmised"""
    def __init__(self):
        self.teadmised = []
    def opib(self, *info):
        """Õpetab info õpilasele, vajab õpetava info"""
        self.teadmised.append(info)
    def unustab(self):
        """Kustutab teadmised õpilase objektist"""
        print("Õpilane teab neid teemasid: ")
        for new_lst in self.teadmised:
            print(new_lst, end=',')
        print("\n")
        pikkus = len(self.teadmised)-1
        ununeb = randint(0, pikkus)
        sleep(5)
        print("oih, õpliane unustas teema: " + str(self.teadmised[ununeb])[2:-3])
        self.teadmised.pop(ununeb)
