from models.layanan import Layanan

class Premium(Layanan):

    def hitung_biaya(self):
        return self.harga + 50000