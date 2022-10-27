# Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi,
# joka saa parametrinaan nopeuden muutoksen (km/h).
# Jos nopeuden muutos on negatiivinen, auto hidastaa.
# Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
# Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi
# eikä alentua nollaa pienemmäksi.
# Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h,
# sitten +70 km/h ja lopuksi +50 km/h.
# Tulosta tämän jälkeen auton nopeus.
# Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja
# tulosta uusi nopeus.
# Kuljettua matkaa ei tarvitse vielä päivittää.

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


auto = Auto("ABC-123", 142) #rekisteritunnus , huippunopeus
auto.nopeusNyt = 0
auto.kuljettu_matka = 0
auto.nopeusNyt = auto.kiihdyta(30)
auto.nopeusNyt = auto.kiihdyta(70)
auto.nopeusNyt = auto.kiihdyta(50)
print(f"Auton tämänhetkinen nopeus on: {auto.nopeusNyt} km/h.")
auto.nopeusNyt = auto.kiihdyta(-200)
print(f"Auton tämänhetkinen nopeus on: {auto.nopeusNyt} km/h.")

#print(f"Auton rekisteritunnus on: {auto.rekisteritunnus}.")
#print(f"Auton huippunopeus on: {auto.huippunopeus} km/h.")
#print(f"Auton tämänhetkinen nopeus on: {auto.nopeusNyt} km/h.")
#print(f"Auton kuljettu matka on: {auto.kuljettu_matka} km.")