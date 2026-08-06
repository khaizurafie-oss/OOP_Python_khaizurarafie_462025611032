class Layanan:

    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def hitung_biaya(self):
        return self.harga