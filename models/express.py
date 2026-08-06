from models.layanan import Layanan

class Express(Layanan):

    def hitung_biaya(self):
        return self.harga + 20000