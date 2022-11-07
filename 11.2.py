# Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto.
# Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina.
# Polttomoottoriauton ominaisuutena on bensatankin koko litroina. Kirjoita aliluokille alustajat.
# Esimerkiksi sähköauton alustaja saa parametreinaan
# rekisteritunnuksen, huippunopeuden ja akkukapasiteetin.
# Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman kapasiteettinsa.
# Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh)
# ja yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l). Aseta kummallekin autolle haluamasi nopeus,
# käske autoja ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat.
import random
class Auto:
    def __init__(self, nopeus, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettumatka = 0

    def kiihdyta(self):
        kiihdytys = random.randint(-10,15)
        self.nopeus = (self.nopeus + kiihdytys)
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.kiihdyta()
        self.kuljettumatka = (self.nopeus * tunnit)

class Sahkoauto(Auto):
    def __init__(self,rekisteritunnus, huippunopeus, akkukapasiteetti):
        self.nopeus = 150
        super().__init__(self.nopeus, rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

    def tulosta_tiedot(self):
        print(f"Sähkäauton: {self.rekisteritunnus}  Huippunopeus: {self.huippunopeus}(km/h)  Akkukapasiteetti: {self.akkukapasiteetti}(kWh)")
        print(f"Nopeus: {self.nopeus}(km/h)  Matkamittarilukema: {self.kuljettumatka}(km)")
        print("----------------------------------------------------------------------------------")

class Polttomoottoriauto(Auto):
    def __init__(self,rekisteritunnus, huippunopeus, bensatankin_koko):
        self.nopeus = 150
        super().__init__(self.nopeus, rekisteritunnus, huippunopeus)
        self.bensatankin_koko = bensatankin_koko

    def tulosta_tiedot(self):
        print(f"Polttomoottoriauton: {self.rekisteritunnus}  Huippunopeus: {self.huippunopeus}(km/h)  Bensatankin koko: {self.bensatankin_koko}(l)")
        print(f"Nopeus: {self.nopeus}(km/h)  Matkamittarilukema: {self.kuljettumatka}(km)")
        print("----------------------------------------------------------------------------------")

sahkoauto = Sahkoauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)
sahkoauto.kulje(3)
polttomoottoriauto.kulje(3)
sahkoauto.tulosta_tiedot()
polttomoottoriauto.tulosta_tiedot()