import random
import string

class SecurePasswordGenerator:
    def _init_(self, length):
        self.length = length
        self.characters = string.ascii_letters + string.digits + string.punctuation

    def create_password(self):
        if self.length < 1:
            return "Password length must be at least 1 character."


        password = ''.join(random.choice(self.characters) for _ in range(self.length))
        return password

class PasswordController:
    def _init_(self):
        self.password_generator = None

    def request_password_length(self):
        try:
            length = int(input("Please specify the length of the password: "))
            return length
        except ValueError:
            print("Invalid input. Please provide a numeric value for the length.")
            return None

    def execute(self):
        length = self.request_password_length()
        if length is not None:
            self.password_generator = SecurePasswordGenerator(length)
            password = self.password_generator.create_password()
            print("Your new password is:", password)

controller = PasswordController()
controller.execute()
