from datetime import datetime
class Grade:
    all_grades = []
    def __init__(self, id, student_id, subject, value, date, teacher_id, comment=None):
        self.id = id
        self.student_id = student_id
        self.subject = subject
        self.value = value
        self.date = date    # ISO 8601 format string
        self.teacher_id = teacher_id
        self.commment = comment
        Grade.all_grades.append(value)

    def update_grade(self, value):
        if 1 <= value <= 5:
            old_value = self.value
            self.value = value
            self.date = datetime.now().date().isoformat()  # Update the date to current
            return f"Grade updated from {old_value} to {self.value}."
        else:
            return "Invalid grade value. Must be between 1 and 5."

    def get_grade_info(self):
        return {
            "grade_id": self.id,
            "student_id": self.student_id,
            "subject": self.subject,
            "grade": self.value,
            "date": self.date,
            "teacher_id": self.teacher_id
        }
    
    @classmethod
    def get_stats(cls):
        return f"Average : {sum(cls.all_grades)/len(cls.all_grades)}\nMax : {max(cls.all_grades)}\nMin: {min(cls.all_grades)}"
    
    def give_comment(self, comment):
        self.commment = comment
