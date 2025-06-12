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

    def update_profile():
        pass

class User(AbstractRole):
    def __init__(self, id, full_name, email, password_hash, created_at, role, notifications):
        super.__init__(id, full_name, email, password_hash, created_at)
        self.role = role
        self._notifications = notifications

    def get_profile():
        pass

    def update_profile():
        pass

    def add_notification(message):
        pass

    def view_notifications():
        pass

    def delete_notification(id):
        pass



