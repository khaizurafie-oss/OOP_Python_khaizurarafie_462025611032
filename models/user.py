class User:

    def __init__(self, nama, username, password):
        self.__nama = nama
        self.__username = username
        self.__password = password

    def get_nama(self):
        return self.__nama

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def set_password(self, password_baru):
        self.__password = password_baru

    def login(self):
        return f"{self.__nama} berhasil login"

    def __str__(self):
        return self.__nama
    