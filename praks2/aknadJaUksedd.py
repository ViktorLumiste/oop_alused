from aknadjaUksed import *
tuba1 = Tuba(int(input("Sisestage esimese toa pikkus: ")),int(input("Sisestage esimese toa laius: ")),int(input("Sisestage esimese toa kõrgus: ")))
valik = (input("Kas soovite lisada aknad või uksed? ")).lower()
while valik == "jah":
    tuba1.lisaAkenUks(int(input("Sisestage akna või ukse laius: ")),int(input("Sisestage akna või ukse kõrgust: ")))
    valik = input("Kas soovite lisada veel aknaid või uksi? ").lower()
tuba1.tapp_rull(int(input("Sisestage kasutava tapeedirulli pikkust: ")), int(input("Sisestage kasutava tapeedirulli laiust: ")))
tuba1.tooPind()