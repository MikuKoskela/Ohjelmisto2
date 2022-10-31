# Jatka edellisen tehtävän ohjelmaa siten,
# että Talo-luokassa on parametriton metodi palohälytys,
# joka käskee kaikki hissit pohjakerrokseen.
# Jatka pääohjelmaa siten, että talossasi tulee palohälytys.

class Hissi:
    def __init__(self, hissi_numero, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissi_numero = hissi_numero
        self.kerros = 0

    def kerros_ylös(self, hissi_numero):
        self.kerros += 1
        print(f"Hissi {hissi_numero} on kerroksessa: {self.kerros}")
        return self.kerros

    def kerros_alas(self, hissi_numero):
        self.kerros -= 1
        print(f"Hissi {hissi_numero} on kerroksessa: {self.kerros}")
        return self.kerros

    def siirry_kerrokseen(self, hissi_numero, haluttu_kerros):
        if haluttu_kerros <= self.ylin_kerros and haluttu_kerros >= self.alin_kerros:
            while self.kerros != haluttu_kerros:
                if self.kerros < haluttu_kerros:
                    self.kerros = self.kerros_ylös(hissi_numero)
                elif self.kerros > haluttu_kerros:
                    self.kerros = self.kerros_alas(hissi_numero)
                if self.kerros == haluttu_kerros:
                    print(f"Hissi {hissi_numero} on saapunut kerrokseen: {self.kerros}")
        else:
            print("Kerrosta ei ole olemassa")


class Talo:

    def __init__(self, alin_kerros, ylin_kerros, hissit_lkm):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit_lkm = int(hissit_lkm)
        self.hissit = []
        for hissi in range(1, (hissit_lkm) + 1):
            self.hissi = Hissi({int(len(self.hissit))}, self.alin_kerros, self.ylin_kerros)
            self.hissit.append(hissi)

    def aja_hissiä(self, hissi_numero, haluttu_kerros):
        if hissi_numero == 1:
            Hissi.siirry_kerrokseen(t.hissi, hissi_numero, haluttu_kerros)
        elif hissi_numero == 2:
            Hissi.siirry_kerrokseen(t.hissi, hissi_numero, haluttu_kerros)
        elif hissi_numero == 3:
            Hissi.siirry_kerrokseen(t.hissi, hissi_numero, haluttu_kerros)
        elif hissi_numero == 4:
            Hissi.siirry_kerrokseen(t.hissi, hissi_numero, haluttu_kerros)
        elif hissi_numero == 5:
            Hissi.siirry_kerrokseen(t.hissi, hissi_numero, haluttu_kerros)

    def palohälytys(self):
        h = int(len(t.hissit))
        for x in t.hissit:
            if x < h:
                t.aja_hissiä(x, 0)
                x = x + 1
                print(f"Hissi {x} on siirtynyt kerrokseen {t.hissi.kerros}")

t = Talo(0, 10, 5)
t.aja_hissiä(1, 4)
t.aja_hissiä(2, 2)
t.aja_hissiä(3, 4)
t.aja_hissiä(4, 6)
t.aja_hissiä(5, 8)

t.palohälytys()

