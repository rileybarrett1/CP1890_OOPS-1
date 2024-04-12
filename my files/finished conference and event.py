class Conference(Event):
    def __init__(self):
        super().__init__(name="Tech Conference",
                         start_time=datetime(2023, 9, 15, hour=0, minute=0, second=0),
                         end_time=datetime(2023, 9, 17, hour=23, minute=59, second=59),
                         location="San Francisco")

    def duration(self):
        if self.start_time and self.end_time:
            return (self.end_time - self.start_time).total_seconds() / 3600  # Convert seconds to hours
        else:
            return None

if __name__ == "__main__":
    # my_event = Event(name="Birthday Party",
    #                  start_time=datetime(2023, 8, 25),
    #                  end_time=datetime(2023, 8, 26),
    #                  location="New York",
    #                  )
    my_conference = Conference()

    print("")
    print("Event:                                    Conference:")
    print(f"Name: {my_event.name}                      Name: {my_conference.name}")
    print(f"Location: {my_event.location}                        Location: {my_conference.location}")
    print(f"Start Time: {my_event.start_time.strftime('%y-%m-%d')}                      Start Time: {my_conference.start_time.strftime('%y-%m-%d')}")
    print(f"End Time: {my_event.end_time.strftime('%y-%m-%d')}                        End Time: {my_conference.end_time.strftime('%y-%m-%d')}")
    print(f"Duration(days): {my_event.duration()}                         attendees=500")
    print(f"                                          Duration(hours): {my_conference.duration()}")
