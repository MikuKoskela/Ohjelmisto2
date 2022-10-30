# Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman
# ja ylimmän kerroksen numeron. Hissillä on metodit siirry_kerrokseen,
# kerros_ylös ja kerros_alas. Uusi hissi on aina alimmassa kerroksessa.
# Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5),
# metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta kertaa,
# että hissi päätyy viidenteen kerrokseen.
# Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin
# ja ilmoittavat, missä kerroksessa hissi sen jälkeen on.
# Testaa luokkaa siten, että teet pääohjelmassa hissin ja
# käsket sen siirtymään haluamaasi kerrokseen
# ja sen jälkeen takaisin alimpaan kerrokseen.


class Hissi:
    def __init__(self,alin_kerros,ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = 0

    def kerros_ylös(self):
        h.kerros += 1
        print(f"Hissi on kerroksessa: {h.kerros}")
        return h.kerros
    def kerros_alas(self):
        h.kerros -= 1
        print(f"Hissi on kerroksessa: {h.kerros}")
        return h.kerros
    def siirry_kerrokseen(self,haluttu_kerros):
        if haluttu_kerros <= h.ylin_kerros and haluttu_kerros >= h.alin_kerros:
            while h.kerros != haluttu_kerros:
                if h.kerros < haluttu_kerros:
                    h.kerros = h.kerros_ylös()
                elif h.kerros > haluttu_kerros:
                    h.kerros = h.kerros_alas()

                if h.kerros == haluttu_kerros:
                    print(f"Hissi on saapunut kerrokseen: {h.kerros}")
        else:
            print("Kerrosta ei ole olemassa")
h = Hissi(0,10)

h.siirry_kerrokseen(6)
h.siirry_kerrokseen(3)
h.siirry_kerrokseen(11)
h.siirry_kerrokseen(-1)
h.siirry_kerrokseen(8)





