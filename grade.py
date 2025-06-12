class Grade:
    def __init__(self, id, student_id, subject, value, date, teacher_id):
        self.id = id
        self.student_id = student_id
        self.subject = subject
        self.value = value  # Expected to be an int between 1–5
        self.date = date    # ISO 8601 format string
        self.teacher_id = teacher_id

    def update_grade(self, value):
        """Bahoni yangilash"""
        pass

    def get_grade_info(self):
        """Baho haqida ma'lumot"""
        pass
