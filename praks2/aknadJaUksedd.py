from aknadjaUksed import *
tuba1 = Tuba(input("Sisestage esimese toa pikkus"),input("Sisestage esimese toa laius"),input("Sisestage esimese toa kõrgus"))
valik = input("Kas soovite lisada aknad või uksed?")
while valik == "jah":
    tuba1.lisaAkenUks(input("Sisestage akna või ukse laius"),input("Sisestage akna või ukse kõrgust"))
    valik = input("Kas soovite lisada veel aknaid või uksi?")
tuba1.tapp_rull(input("Sisestage kasutava tapeedirulli pikkust"), input("Sisestage kasutava tapeedirulli laiust"))
tuba1.tooPind()