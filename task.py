import datetime

class Task:
    def __init__(self, id: int, description: str, post_date: datetime.datetime, completed: bool, priority: int=10):
        self.id = id
        self.description = description
        self.post_date = post_date
        self.completed = completed
        self.priority = priority

    def __str__(self):
        # returns a string of the date, description, priority and if it is completed
        return (f"Task(ID: {self.id}, Description: '{self.description}', "
                f"Due: {self.post_date.strftime('%Y-%m-%d %H:%M')}, "
                f"Completed:{self.completed}, Priority: {self.priority}")

    def update_priority(self):
        # method will see if the due date is within 1 week of our current date
        # if so, update the priority to 1
        now = datetime.datetime.now()
        time_diff = self.post_date - now
        if time_diff.days <= 7:
            self.priority = 1

