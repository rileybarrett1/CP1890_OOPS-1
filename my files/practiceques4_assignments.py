from datetime import datetime, date
from dataclasses import dataclass


# creating the task class setting attributes name,description and due date
# setting this as our dataclass
@dataclass
class Task:

    def __init__(self):
        self.task_name: str
        self.task_description: str
        self.due_date = None

    # creating the status if due date is greater than today return pending if not return completed
    # making it a property of the dataclass
    @property
    def status(self):
        if self.due_date > datetime.today():
            return "Pending"
        else:
            return "Completed"


# making a class for homework
class Homework(Task):
    # putting my innit method and importing the data from my dataclass while setting new attributes
    def __init__(self):
        super().__init__()
        self.subject: str = "Math"
        self.task_name: str = "Math homework"
        self.task_description: str = "Complete exercises 1-5"
        self.due_date = datetime(year=2023, month=10, day=15, hour=0, minute=0, second=0, microsecond=0)
        self.done: bool = False

    # overriding the status to return what I want for this class
    def status(self):
        if not self.done:
            return "Not started"
        elif self.done and self.due_date > datetime.today():
            return "In progress"
        else:
            return "Completed"


# creating a class for meeting
class Meeting(Task):
    # putting my innit method and importing the data from my dataclass while setting new attributes
    def __init__(self):
        super().__init__()
        self.task_name: str = "Team meeting"
        self.task_description: str = "Discuss project updates"
        self.due_date: date = datetime(year=2023, month=9, day=20, hour=0, minute=0, second=0, microsecond=0)
        self.location: str = "Office A"

    # overriding the status to return what I want for this class
    def status(self):
        if self.due_date > datetime.today():
            return "Scheduled"
        else:
            return "Happened"


# to run the code
if __name__ == "__main__":
    homework = Homework()
    meeting = Meeting()

    # printing everything out and formatting it
    print("")
    print("Homework:")
    print(f"Task Name:{homework.task_name}")
    print(f"Task Description:{homework.task_description}")
    print(f"Due Date:{homework.due_date}")
    print(f"Subject:{homework.subject}")
    print(f"Status:{homework.status()}")
    print("\n")
    print("Meeting:")
    print(f"Task Name:{meeting.task_name}")
    print(f"Task Description:{meeting.task_description}")
    print(f"Due Date:{meeting.due_date}")
    print(f"Location:{meeting.location}")
    print(f"Status:{meeting.status()}")
