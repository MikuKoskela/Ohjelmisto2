# Kirjoita Auto-luokka, jonka ominaisuuksina ovat
# rekisteritunnus, huippunopeus, tämänhetkinen nopeus ja kuljettu matka.
# Kirjoita luokkaan alustaja,
# joka asettaa ominaisuuksista kaksi ensin mainittua parametreina
# saatuihin arvoihin.
# Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi.
# Kirjoita pääohjelma,
# jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h).
# Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
auto = Auto("ABC-123", 142) #rekisteritunnus , huippunopeus
auto.nopeusNyt = 0
auto.kuljettu_matka = 0


print(f"Auton rekisteritunnus on: {auto.rekisteritunnus}.")
print(f"Auton huippunopeus on: {auto.huippunopeus} km/h.")
print(f"Auton tämänhetkinen nopeus on: {auto.nopeusNyt} km/h.")
print(f"Auton kuljettu matka on: {auto.kuljettu_matka} km.")

