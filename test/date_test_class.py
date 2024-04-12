import datetime
from datetime import time


class countdown():
   #  creating he objects of time and having todays date with a stop date
   def __init__(self):
       self.count = 0
       self.start_time = datetime.datetime.now()
       self.end_time = datetime.date.strftime("%Y-%m-%d")


   #  setting time left as a property and returning how much time is left
   @property
   def time_left(self):
        return self.end_time - self.start_time

   #  if time is expired it will return false other wise it will reeturn true
   @property
   def is_expired(self):
       if self.time_left == 0:
           return False
       else:
           return True

    # def increment(self):
    #     self.time_left.total_seconds()
