from sodurid2 import Sodur
from random import randint
armee_1 = []
armee_2 = []
armee_1_id = []
armee_2_id = []
for a in range(1,21):
    armee_va = randint(1,2)
    if armee_va == 1:
        armee_1.append(Sodur(armee_va))
    else:
        armee_2.append(Sodur(armee_va))
for sodur in armee_1:
    armee_1_id.append(sodur.id)
for sodur in armee_2:
    armee_2_id.append(sodur.id)
print("1.armees on sõdurid id-ga " + ", " .join((map(str,armee_1_id))))
print("2.armees on sõdurid id-ga " +", ".join((map(str,armee_2_id))))

