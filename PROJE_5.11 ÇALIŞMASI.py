class Kisi:
    def __init__(self, ad, yas):
        self.ad = ad
        self.yas = yas

    def bilgileri_goster(self):
        return f"Ad: {self.ad}, Yaş: {self.yas}"

class Ogrenci(Kisi):
    def __init__(self, ad, yas, ogrenci_numarasi):
        super().__init__(ad, yas)
        self.ogrenci_numarasi = ogrenci_numarasi

    def bilgileri_goster(self):
        return f"{super().bilgileri_goster()}, Öğrenci Numarası: {self.ogrenci_numarasi}"

class Ogretmen(Kisi):
    def __init__(self, ad, yas, ders):
        super().__init__(ad, yas)
        self.ders = ders

    def bilgileri_goster(self):
        return f"{super().bilgileri_goster()}, Ders: {self.ders}"

# Örnek Kullanım
ogrenci = Ogrenci("Mehmet", 22, "M98765")
ogretmen = Ogretmen("Zeynep", 35, "Fizik")

print(ogrenci.bilgileri_goster())
print(ogretmen.bilgileri_goster())
