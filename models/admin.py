from models.user import User

class Admin(User):

    def login(self):
        return "Login sebagai Admin"
    