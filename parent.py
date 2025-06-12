from .user import User

class Parent(User):
    def __init__(self, id, full_name, email, password_hash, created_at, role, notifications, children=None):
        super().__init__(id, full_name, email, password_hash, created_at, role, notifications)
        self.children = children if children is not None else []  # List of student IDs
        
    def view_child_grades(self, child_id):
        """Farzandning baholarini ko‘rish"""
        pass

    def view_child_assignments(self, child_id):
        """Farzandning vazifalarini ko‘rish"""
        pass

    def receive_child_notification(self, child_id):
        """Farzand haqidagi xabarnomalarni olish"""
        pass
