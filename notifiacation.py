from admin import all_users

class Notification:
    def __init__(self, id, message, recipient_id, created_at):
        self.id = id
        self.message = message
        self.recipient_id = recipient_id
        self.created_at = created_at  # ISO 8601 format string
        self._is_read = False

    def send(self):
        for user in all_users:
            if user._id == self.recipient_id:
                user.add_notifactions(self.message)
                return "Notification sent successfully"
            else: 
                return "User with this id  does not exist"
            

    def mark_as_read(self):
        self._is_read = True
