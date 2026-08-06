class Sepatu:

    def __init__(self, merk, warna, ukuran):
        self.__merk = merk
        self.__warna = warna
        self.__ukuran = ukuran

    def get_merk(self):
        return self.__merk

    def get_warna(self):
        return self.__warna

    def get_ukuran(self):
        return self.__ukuran