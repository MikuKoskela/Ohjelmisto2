# Laajenna ohjelmaa siten, että mukana on kulje-metodi,
# joka saa parametrinaan tuntimäärän.
# Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla
# annetussa tuntimäärässä edennyt.
# Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km.
# Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa
# kuljetun matkan lukemaan 2090 km.
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

auto = Auto("ABC-123", 142) #rekisteritunnus , huippunopeus
auto.tunnit = 0
auto.nopeusNyt = 60
auto.kuljettu_matka = 2000
#auto.nopeusNyt = auto.kiihdyta(30)
#auto.nopeusNyt = auto.kiihdyta(70)
#auto.nopeusNyt = auto.kiihdyta(50)
#print(f"Auton tämänhetkinen nopeus on: {auto.nopeusNyt} km/h.")
#auto.nopeusNyt = auto.kiihdyta(-200)
#print(f"Auton tämänhetkinen nopeus on: {auto.nopeusNyt} km/h.")
auto.kuljettu_matka = int(auto.kulje(1.5))
#print(f"Auton rekisteritunnus on: {auto.rekisteritunnus}.")
#print(f"Auton huippunopeus on: {auto.huippunopeus} km/h.")
#print(f"Auton tämänhetkinen nopeus on: {auto.nopeusNyt} km/h.")
print(f"Auton kuljettu matka on: {auto.kuljettu_matka} km.")