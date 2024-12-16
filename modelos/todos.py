class Todo:
    def __init__(self, id, user_id, title, completed):
        self.id = id
        self.user_id = user_id
        self.title = title
        self.completed = completed

    def __str__(self):
        return f"[Todo] ID: {self.id}, User ID: {self.user_id}, Title: {self.title}, Completed: {self.completed}"

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "title": self.title,
            "completed": self.completed
        }
