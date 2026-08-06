class pelanggan:

    def __init__(self, id_pelanggan, nama, no_hp):
        self.__id = id_pelanggan
        self.__nama = nama
        self.__no_hp = no_hp

    def get_id(self):
        return self.__id

    def get_nama(self):
        return self.__nama

    def get_no_hp(self):
        return self.__no_hp

    def __str__(self):
        return self.__nama