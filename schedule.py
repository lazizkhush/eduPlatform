class Schedule:
    def __init__(self, id, class_id, day):
        self.id = id
        self.class_id = class_id
        self.day = day  # e.g., "Monday", "Tuesday", etc.
        self.lessons = {}  # {time: {"subject": str, "teacher_id": int}}

    def add_lesson(self, time, subject, teacher_id):
        """Dars qo‘shish"""
        pass

    def view_schedule(self):
        """Jadvalni ko‘rish"""
        pass

    def remove_lesson(self, time):
        """Darsni o‘chirish"""
        pass
