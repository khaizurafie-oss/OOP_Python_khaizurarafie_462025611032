from models.layanan import Layanan

class Reguler(Layanan):

    def hitung_biaya(self):
        return self.harga
    