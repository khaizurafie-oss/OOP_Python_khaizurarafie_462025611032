class Transaksi:

    def __init__(self, pelanggan, layanan, status):
        self.pelanggan = pelanggan
        self.layanan = layanan
        self.status = status

    def ubah_status(self, status_baru):
        self.status = status_baru