from .user import User

all_users = []  # Global list of all User objects

class Admin(User):
    def __init__(self, id, full_name, email, password_hash, created_at, role, notifications, user_registry, permissions=None):
        super().__init__(id, full_name, email, password_hash, created_at, role, notifications)
        self.permissions = permissions if permissions is not None else []
        self.user_registry = user_registry if user_registry is not None else {}  # {user_id: User}

    def add_user(self, user):
        for existing_user in all_users:
            if existing_user._id == user._id:
                return f"User with ID {user._id} already exists."
        all_users.append(user)
        return f"User {user._full_name} added successfully."

    def remove_user(self, user_id):
        for user in all_users:
            if user._id == user_id:
                all_users.remove(user)
                return f"User {user._full_name} removed."
        return f"No user found with ID {user_id}."

    def generate_report(self):
        if not all_users:
            return "No users in the system."
        report_lines = ["User Report:"]
        for user in all_users:
            report_lines.append(f"- {user._full_name} (ID: {user._id}, Role: {user.role})")
        return "\n".join(report_lines)

