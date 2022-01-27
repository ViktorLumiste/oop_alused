from sodurid2 import Sodur
from random import randint
armee_1 = []
armee_2 = []
for a in range(1,21):
    armee_va = randint(1,2)
    if armee_va == 1:
        armee_1.append(Sodur(armee_va))
    else:
        armee_2.append(Sodur(armee_va))