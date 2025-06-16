from user import User

class Parent(User):
    def __init__(self, id, full_name, email, password_hash, created_at, role, notifications, children=None):
        super().__init__(id, full_name, email, password_hash, created_at, role, notifications)
        self.children = children if children is not None else []
        

    def view_child_grades(self, child_id):
        for child in self.children:
            if child._id == child_id:
                return child.view_grades()
        return f"No child with ID {child_id} found."

    def view_child_assignments(self, child_id):
        for child in self.children:
            if child._id == child_id:
                return child.assignments
        return f"No child with ID {child_id} found."

    def receive_child_notification(self, child_id):
        for child in self.children:
            if child._id == child_id:
                return child.view_notifications()
        return f"No child with ID {child_id} found."