class Todo:
    def __init__(self, user_id, id, title, completed):
        self.user_id = user_id
        self.id = id
        self.title = title
        self.completed = completed

    def __str__(self):
        return f"[Todo] ID: {self.id}, Title: {self.title}, Completed: {self.completed}"

    def to_dict(self):
        """aqui se convierte el objeto Todo en un diccionario"""
        return {
            "userId": self.user_id,
            "id": self.id,
            "title": self.title,
            "completed": self.completed
        }