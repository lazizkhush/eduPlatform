class Assignment:
    def __init__(self, id, title, description, deadline, subject, teacher_id, class_id):
        self.id = id
        self.title = title
        self.description = description
        self.deadline = deadline  # ISO 8601 format string
        self.subject = subject
        self.teacher_id = teacher_id
        self.class_id = class_id
        self.submissions = {}  # {student_id: content}
        self.grades = {}       # {student_id: grade}

    def add_submission(self, student_id, content):
        """O‘quvchi javobini qo‘shish"""
        pass

    def set_grade(self, student_id, grade):
        """Baho qo‘yish"""
        pass

    def get_status(self):
        """Vazifa holatini ko‘rish"""
        pass
