class User:
    def __init__(self, id, name, username, email):
        self.id = id
        self.name = name
        self.username = username
        self.email = email

    def __str__(self):
        return f"[User] ID: {self.id}, Name: {self.name}, Email: {self.email}"

    def to_dict(self):
        """
        Se convierte en un diccionario"""
        return {
            "id": self.id,
            "name": self.name,
            "username": self.username,
            "email": self.email
        }