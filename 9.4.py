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
    def kiihdyta(self, nopeuden_muutos):
        if nopeuden_muutos == -200:
            nopeusNyt = 0
            return nopeusNyt
        if nopeuden_muutos > 0:
            nopeusNyt = auto.nopeusNyt + nopeuden_muutos
            if nopeusNyt > auto.huippunopeus:
                nopeusNyt = 142
                return nopeusNyt
            return nopeusNyt
    def kulje(self, tunnit):
        kuljettu_matka = auto.nopeusNyt * tunnit
        auto.kuljettu_matka = auto.kuljettu_matka + kuljettu_matka
        return auto.kuljettu_matka
autot = ["ABC-1","ABC-2","ABC-3","ABC-4","ABC-5","ABC-6","ABC-7","ABC-8","ABC-9","ABC-10"]
huippunopeus = int(random.randint(100,200))

for i in range(0,11):
    rekisteritunnus = autot[0]
    auto = Auto(rekisteritunnus, huippunopeus) #rekisteritunnus , huippunopeus

auto.nopeusNyt = 60
auto.kuljettu_matka = 2000
print(i)

print(f"Auton rekisteritunnus on: {auto.rekisteritunnus}.")
print(f"Auton huippunopeus on: {auto.huippunopeus} km/h.")
print(f"Auton tämänhetkinen nopeus on: {auto.nopeusNyt} km/h.")
print(f"Auton kuljettu matka on: {auto.kuljettu_matka} km.")
