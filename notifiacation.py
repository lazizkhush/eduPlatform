class Notification:
    def __init__(self, id, message, recipient_id, created_at):
        self.id = id
        self.message = message
        self.recipient_id = recipient_id
        self.created_at = created_at  # ISO 8601 format string
        self._is_read = False         # Optional internal flag

    def send(self):
        """Xabarni yuborish"""
        pass

    def mark_as_read(self):
        """O‘qilgan deb belgilash"""
        self._is_read = True
