from .user import User
from .assignment import Assignment

class Teacher(User):
    def __init__(self, id, full_name, email, password_hash, created_at, role, notifications, subjects, classes, assignments):
        super().__init__(id, full_name, email, password_hash, created_at, role, notifications)
        self.subjects = subjects
        self.classes = classes
        self.assignments = assignments

    def create_assignment(self, title, description, deadline, subject, class_id):
        new_id = len(self.assignments) + 1  # Simple auto-increment ID
        assignment = Assignment(
            id=new_id,
            title=title,
            description=description,
            deadline=deadline,
            subject=subject,
            teacher_id=self._id,
            class_id=class_id
        )
        self.assignments.append(assignment)
        
    def grade_assignment(self, assignment_id, student_id, grade):
        """Assign a grade to a student's submission"""
        for assignment in self.assignments:
            if assignment.id == assignment_id:
                assignment.set_grade(student_id, grade)
                return True
        return False

    def view_student_progress(self, student_id):
        progress = []
        for assignment in self.assignments:
            if student_id in assignment.submissions:
                submission = assignment.submissions[student_id]
                grade = assignment.grades.get(student_id)
                progress.append({
                    "assignment_title": assignment.title,
                    "submission": submission,
                    "grade": grade
                })
        return progress