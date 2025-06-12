from .user import User

class Teacher(User):
    def __init__(self, id, full_name, email, password_hash, created_at, role, notifications, subjects, classes, assignments):
        super().__init__(id, full_name, email, password_hash, created_at, role, notifications)
        self.subjects = subjects
        self.classes = classes
        self.assignments = assignments

    def create_assignment(title, description, deadline, subject, class_id):
        pass

    def grade_assignment(assignment_id, student_id, grade):
        pass

    def view_student_progress(student_id):
        pass
    