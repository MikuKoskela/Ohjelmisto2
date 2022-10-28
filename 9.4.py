# Nyt ohjelmoidaan autokilpailu.
# Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
# Tee pääohjelman alussa lista,
# joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
# Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä.
# Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa.
# Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:
# Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan
# -10 ja +15 km/h väliltä. Tämä tehdään kutsumalla kiihdytä-metodia.
# Kaikkia autoja käsketään liikkumaan yhden tunnin ajan.
# Tämä tehdään kutsumalla kulje-metodia.
# Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
# Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.
import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettumatka = 0

    def tulosta_tiedot(self):
        print(f"Rekisteritunnus:{self.rekisteritunnus}  Huippunopeus:{self.huippunopeus}km/h.  Tämänhetkinen nopeus:{self.nopeus}km/h.  Kuljettu matka:{self.kuljettumatka}km.")



    def kiihdyta(self, tunnit):
        self.nopeus += tunnit
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0
    def kulje(self, tunnit):
        self.kuljettumatka += (tunnit * self.nopeus)
#auto = Auto("ABC-123", 142) #rekisteritunnus , huippunopeus
#auto.tulosta_tiedot()

autot =[]
for i in range(10): # Joko str(i+1) tai range(1,11)
    autot.append(Auto("ABC-" + str(i+1), random.randint(100,200)))

loppu = False
while not loppu:
    for auto in autot:
        auto.kiihdyta(random.randint(-10,15))
        auto.kulje(1)
        if auto.kuljettumatka >= 10000:
            loppu = True
for auto in autot:
    auto.tulosta_tiedot()

#KORJATTU TUNNILLA
