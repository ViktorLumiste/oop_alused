from tootajad import Inimene
inimene1 = Inimene("Olaf Olev", "Alakivi", 6)
inimene2 = Inimene("Gervin", "Luide", 7)
inimene3 = Inimene("Danil", "Kersontsev", 4)

inimene1.tutvustus()
inimene2.tutvustus()
inimene3.tutvustus()

if inimene1.kutse_kval < inimene2.kutse_kval and inimene1.kutse_kval < inimene3.kutse_kval:
    print(inimene1.enimi,inimene1.pnimi, ", te olite vallandatud")
    del inimene1
elif inimene2.kutse_kval < inimene1.kutse_kval and inimene2.kutse_kval < inimene3.kutse_kval:
    print(inimene2.enimi, inimene2.pnimi, ", te olite vallandatud")
    del inimene2
elif inimene3.kutse_kval < inimene1.kutse_kval and inimene3.kutse_kval < inimene2.kutse_kval:
    print(inimene3.enimi, inimene3.pnimi, ", te olite vallandatud")
    del inimene3
input()
