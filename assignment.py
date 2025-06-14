from datetime import datetime
class Assignment:
    def __init__(self, id, title, description, deadline, subject, teacher_id, class_id, difficulty=None):
        self.id = id
        self.title = title
        self.description = description
        self.deadline = deadline  # ISO 8601 format string
        self.subject = subject
        self.teacher_id = teacher_id
        self.class_id = class_id
        self.submissions = {}  # {student_id: content}
        self.grades = {}       # {student_id: grade}
        self.difficulty = difficulty

    def add_submission(self, student_id, content):
        if student_id in self.submissions:
            return f"Submission already exists for student {student_id}."
        self.submissions[student_id] = content
        return f"Submission received from student {student_id}."

    def set_grade(self, student_id, grade):
        if student_id not in self.submissions:
            return f"No submission found for student {student_id}."
        self.grades[student_id] = grade
        return f"Grade {grade} set for student {student_id}."

    def get_status(self):
        total = len(self.submissions)
        graded = len(self.grades)
        ungraded = total - graded
        deadline_obj = datetime.fromisoformat(self.deadline)
        status = "Open" if datetime.now() < deadline_obj else "Closed"
        return {
            "assignment_id": self.id,
            "title": self.title,
            "subject": self.subject,
            "total_submissions": total,
            "graded": graded,
            "ungraded": ungraded,
            "deadline": self.deadline,
            "status": status
        }
    
    def set_difficulty(self, difficulty):
        if difficulty.lower() in ['easy', 'medium', 'hard']:
            self.difficulty = difficulty
            return True
        return "Invalid difficulty"