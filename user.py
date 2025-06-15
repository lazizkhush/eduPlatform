from abc import ABC, abstractmethod

class AbstractRole(ABC):
    def __init__(self, id, full_name, email, password_hash, created_at):
        self._id = id
        self._full_name = full_name
        self._email = email
        self._password_hash = password_hash
        self._created_at = created_at

    @abstractmethod
    def get_profile():
        pass
    
    @abstractmethod
    def update_profile():
        pass

class User(AbstractRole):
    def __init__(self, id, full_name, email, password_hash, created_at, role, notifications):
        super.__init__(id, full_name, email, password_hash, created_at)
        self.role = role
        self._notifications = notifications

    def get_profile(self):
        """Return user's profile information as a dictionary"""
        return {
            "id": self._id,
            "full_name": self._full_name,
            "email": self._email,
            "created_at": self._created_at,
            "role": self.role
        }

    def update_profile(self, full_name=None, email=None):
        if full_name:
            self._full_name = full_name
        if email:
            self._email = email

    def add_notification(self, message):
        self._notifications.append(message)

    def view_notifications(self):
        return [n.message for n in self._notifications]

    def delete_notification(self, notification_id):
        self._notifications = [n for n in self._notifications if n.id != notification_id]




