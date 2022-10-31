import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettumatka = 0
        self.voitot = 0

    def kiihdyta(self, tunnit):
        self.nopeus += tunnit
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.kuljettumatka += (tunnit * self.nopeus)

class Kilpailu:
    def __init__(self,kilpailun_nimi,kilometrit,autot):
        self.kilpailun_nimi = kilpailun_nimi
        self.kilometrit = kilometrit
        self.autot = autot

    def aja_tunti(self,autot):
        loppu = False
        while not loppu:
            for auto in autot:
                auto.kiihdyta(random.randint(-10, 15))
                auto.kulje(1)
                return autot

    def tulosta_tilanne(self,autot):
        for auto in autot:
            print(f"Rekisteritunnus:{auto.rekisteritunnus}  Huippunopeus:{auto.huippunopeus}km/h."
                f"  Tämänhetkinen nopeus:{auto.nopeus}km/h.  Kuljettu matka:{auto.kuljettumatka}km."
                f"  Voitot:({auto.voitot})")

    def kilpailu_ohi(self,autot):
        for auto in autot:
            if auto.kuljettumatka >= 8000:
                auto.voitot += 1
                return True
            return False

autot = []

for i in range(10): # Joko str(i+1) tai range(1,11)
    auto = (Auto("ABC-" + str(i+1), random.randint(100,200)))
    autot.append(auto)
for auto in autot:
    k = Kilpailu("Suuri romuralli", auto.kuljettumatka, autot)
    while k.kilpailu_ohi(autot) != True:

        k.tulosta_tilanne(autot)
        k.aja_tunti(autot)
        k.kilpailu_ohi(autot)
# KORJAAN TUNNILLA



