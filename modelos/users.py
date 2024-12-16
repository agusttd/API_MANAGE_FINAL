import bcrypt
import re

class User:
    def __init__(self, id, name, username, email, password=None, address=None, phone=None, website=None, company=None):
        self.id = id
        self.name = name
        self.username = username
        self.email = email
        self.password = self.encrypt_password(password) if password else None
        self.address = address
        self.phone = phone
        self.website = website
        self.company = company

    def encrypt_password(self, password):
        """Encripta la contraseña usando bcrypt"""
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hashed.decode('utf-8')

    def check_password(self, input_password, hashed_password):
        """Verifica si la contraseña ingresada coincide con el hash"""
        return bcrypt.checkpw(input_password.encode('utf-8'), hashed_password.encode('utf-8'))


    def __str__(self):
        return f"[User] ID: {self.id}, Name: {self.name}, Email: {self.email}"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "username": self.username,
            "email": self.email,
            "address": self.address,
            "phone": self.phone,
            "website": self.website,
            "company": self.company
        }

    def validate_email(self, email):
            """Valida que el formato del email sea correcto"""
            email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
            return re.match(email_regex, email) is not None