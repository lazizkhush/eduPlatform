from .user import User

class Student(User):
    def __init__(self, id, full_name, email, password_hash, created_at, role, notifications, grade, subjects, assignments, grades):
        super().__init__(id, full_name, email, password_hash, created_at, role, notifications) 
        self.grade = grade
        self.subjects = subjects
        self.assignments = assignments
        self.grades = grades

    def submit_assignment(self, assignment_id, content):
        self.assignments[assignment_id] = content

    def view_grades(self, subject=None):
        if subject:
            return [grade for grade in self.grades if grade.subject == subject]
        return self.grades

    def calculate_average_grade(self):
        if not self.grades:
            return None
        total = sum(grade.value for grade in self.grades)
        return total / len(self.grades)




