class Schedule:
    def __init__(self, id, class_id, day):
        self.id = id
        self.class_id = class_id
        self.day = day  # e.g., "Monday", "Tuesday", etc.
        self.lessons = {}  # {time: {"subject": str, "teacher_id": int}}

    def add_lesson(self, time, subject, teacher_id):
        if time in self.lessons:
            return f"A lesson already exists at {time}."
        self.lessons[time] = {"subject": subject, "teacher_id": teacher_id}
        return f"Lesson added at {time}: {subject} (Teacher ID: {teacher_id})"

    def view_schedule(self):
        if not self.lessons:
            return f"No lessons scheduled for {self.day}."
        sorted_times = sorted(self.lessons.keys())
        schedule = f"Schedule for {self.day}:\n"
        for time in sorted_times:
            lesson = self.lessons[time]
            schedule += f"  {time}: {lesson['subject']} (Teacher ID: {lesson['teacher_id']})\n"
        return schedule.strip()

    def remove_lesson(self, time):
        if time in self.lessons:
            removed = self.lessons.pop(time)
            return f"Removed lesson at {time}: {removed['subject']}."
        return f"No lesson found at {time} to remove."
    


