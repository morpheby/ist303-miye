
class Room:

    ID = 30000

    def __init__(self, numbr, max_guests):
        self.ID = Room.ID
        Room.ID += 1
        self.numbr = numbr
        self.max_guests = max_guests

    def remove(self, numbr):
        pass
    
    @property
    def name(self):
        "The name property."
        return "Room #%d (max. guests: %d)" % (self.numbr, self.max_guests)
     