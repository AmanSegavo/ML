class Kucing:
    def __init__(self, nama):
        self.nama = nama

    def respon(self):
        return self.nama + " Meong-meong!"
    
class Anjing:
    def __init__(self, nama):
        self.nama = nama

    def respon(self):
        return self.nama + " Gug-gug!"

Heli = Anjing('Heli')
siHeli = Heli.respon()

oyen = Kucing('Oyen')
siOyen = oyen.respon()
print(siOyen)
print(siHeli)

for binatang in [Heli, oyen]:
    print(type(binatang))
    print(binatang.respon())

def hewan_ngomong(binatang):
    print(binatang.respon())

    print(hewan_ngomong(oyen))