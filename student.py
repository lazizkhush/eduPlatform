from .user import User

class Student(User):
    def __init__(self, id, full_name, email, password_hash, created_at, role, notifications, grade, subjects, assignments, grades):
        super().__init__(id, full_name, email, password_hash, created_at, role, notifications) 
        self.grade = grade
        self.subjects = subjects
        self.assignments = assignments
        self.grades = grades

    def submit_assignment(assignment_id, content):
        pass
    
    def view_grades(subject=None):
        pass

    def calculate_average_grade():
        pass



