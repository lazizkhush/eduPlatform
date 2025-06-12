from .user import User

class Admin(User):
    def __init__(self, id, full_name, email, password_hash, created_at, role, notifications, permissions=None):
        super().__init__(id, full_name, email, password_hash, created_at, role, notifications)
        self.permissions = permissions if permissions is not None else []

    def add_user(self, user):
        """Yangi foydalanuvchi qo‘shish"""
        pass

    def remove_user(self, user_id):
        """Foydalanuvchini o‘chirish"""
        pass

    def generate_report(self):
        """Tizim bo‘yicha hisobot yaratish"""
        pass
