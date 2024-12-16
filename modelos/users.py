class User:
    def __init__(self, id, name, username, email, address=None, phone=None, website=None, company=None):
        self.id = id
        self.name = name
        self.username = username
        self.email = email
        self.address = address  
        self.phone = phone      
        self.website = website  
        self.company = company  

    def __str__(self):
        return (f"[User] ID: {self.id}, Name: {self.name}, Email: {self.email}, "
                f"Address: {self.address}, Phone: {self.phone}, Website: {self.website}, Company: {self.company}")

    def to_dict(self):
        """
        Se convierte en un diccionario
        """
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
