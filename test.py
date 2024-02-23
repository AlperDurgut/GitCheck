class Alper:

    def __init__(self, isim, soyisim) -> None:
        self.isim = isim
        self.soyisim = soyisim

a = Alper("Alper", "Durgut")
print(a)
print(a.isim)
print(a.soyisim)

class Aysin(Alper):
    def __init__(self, yas) -> None:
        self.yas = yas
