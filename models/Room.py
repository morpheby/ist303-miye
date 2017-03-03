#creating a new instance with y = Room(405,4) will automatically add the room to the master list of rooms (Room.list_all)

def init_rooms():
    #create the master list of all rooms; list of lists: [room #, max occ.]
    single = [ [100 + x, 1] for x in range(16) ]
    double = [ [200 + x, 2] for x in range(16) ]
    quad = [ [300 + x, 4] for x in range(4) ]
    [Room(r,g) for r,g in single + double + quad]
    

class Room:
    
    list_all = []

    def __init__(self, numbr, max_guests):
        self.numbr = numbr
        self.max_guests = max_guests
        Room.list_all.append(self)

    def remove(self, numbr):
        pass
    
    @property
    def name(self):
        "The name property."
        return "Room #%d (max. guests: %d)" % (self.numbr, self.max_guests)
        
init_rooms()
