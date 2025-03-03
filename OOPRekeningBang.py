class RekeningBank:
    def __init__(self, tabungan):
        self.tabungan = tabungan

    def cek_saldo(self):
        print("Jumlah Saldo Anda adalah = Rp {}".format(self.tabungan))

    def menabung(self):
        tambah = int(input('Masukkan jumlah yang ingin anda tabung = '))
        self.tabungan += tambah

    def menarik(self):
        kurang = int(input("Masukkan jumlah yang ingin anda ambil = "))
        if self.tabungan < kurang:
            print("Maaf saldo anda tidak mencukupi \nSaldo anda saat ini adalah {}").format(self.tabungan)
        else:
            self.tabungan -= kurang

menabung = int(input("Masukkan saldo yang ingin anda masukkan = "))
print(menabung)

tabunganAman = RekeningBank(menabung)
print(tabunganAman.cek_saldo())

print(tabunganAman.menabung())
print(tabunganAman.cek_saldo())


print(tabunganAman.menarik())
print(tabunganAman.cek_saldo())

pertanyaan = input("Apakah anda masih ingin melanjutkan transaksi ini ? (y/n) ")
if pertanyaan == 'y':
    pertanyaan2 =input("transaksi apa yang ingin anda lakukan ?, silahkan pilih: A ->menabung, B -> ceksaldo C ->menarik"))
    if pertanyaan2 == 'A':
        print(tabunganAman.menabung())
    elif: pertanyaan2 == 'B':
        print(tabunganAman.cek_saldo())
