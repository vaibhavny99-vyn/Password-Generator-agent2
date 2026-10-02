import random
import string


class PasswordAgent:

    def generate(self, length, password_type):

        if length < 4:
            return "Password length must be at least 4."

        if password_type == "letters":
            characters = string.ascii_letters

        elif password_type == "numbers":
            characters = string.digits

        elif password_type == "symbols":
            characters = string.punctuation

        elif password_type == "mixed":
            characters = string.ascii_letters + string.digits + string.punctuation

        else:
            return "Use letters, numbers, symbols, or mixed."

        password = ""

        for _ in range(length):
            password += random.choice(characters)

        return password

    def process(self, command):

        parts = command.split()

        if len(parts) == 2:

            try:
                length = int(parts[1])
            except ValueError:
                return "Length must be a number."

            password_type = "mixed"

        elif len(parts) == 3:

            try:
                length = int(parts[1])
            except ValueError:
                return "Length must be a number."

            password_type = parts[2].lower()

        else:
            return "Use: generate 12 or generate 12 letters"

        return self.generate(length, password_type)