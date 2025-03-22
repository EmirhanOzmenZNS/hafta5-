class Hesap:
    def __init__(self, say1, say2):
        self.say1 = say1
        self.say2 = say2

    def carp(self):
        sonuc = self.say1 * self.say2
        return sonuc

    def bol(self):
        if self.say2 != 0:
            sonuc = self.say1 / self.say2
            return sonuc
        else:
            return "Bölen sıfır olamaz"

    def topla(self):
        sonuc = self.say1 + self.say2
        return sonuc

    def cikar(self):
        sonuc = self.say1 - self.say2
        return sonuc

    def yazdir(self):
        toplam = self.topla()
        carpma = self.carp()
        print(f"Sayıların toplamı: {toplam}")
        print(f"Sayıların çarpımı: {carpma}")
