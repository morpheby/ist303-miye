
from .Room import Room
from .Client import Client
from .Reservation import Reservation

class Repository(object):
    __instance = None
    
    def __new__(cls, *args, **kwargs):
        if Repository.__instance is None:
            Repository.__instance = object.__new__(cls, *args, **kwargs)
        return Repository.__instance

    def __init__(self):
        self.rooms = []
        self.clients = []
        self.reservations = []

        #create the master list of all rooms: [room #, max occ.]
        single = [ [100 + x, 1] for x in range(16) ]
        double = [ [200 + x, 2] for x in range(16) ]
        quad = [ [300 + x, 4] for x in range(4) ]
        self.rooms = [Room(r,g) for r,g in single + double + quad]

        self.clients = [Client(*name.split(' ')) for name in ['Test User', "Another One"]]
        self.reservations = [Reservation(c.ID, '1/1/1997', '1/2/1997', 1) for c in self.clients]

    def add_client(self, client):
        self.clients += [client]
    
    def add_reservation(self, reservation):
        self.reservations += [reservation]
    
    def find_client_by_id(self, clientID):
        found = [c for c in self.clients if c.ID == clientID]
        if len(found) == 0:
            return None
        else:
            return found[0]
            
    def find_reservation_by_id(self, resID):
        found = [r for r in self.reservations if r.ID == resID]
        if len(found) == 0:
            return None
        else:
            return found[0]


#Static HOTEL variables
# base prices are weekday, off-season
hotel_baseprice = {'Single': 140, 'Double': 260, 'Quad': 480}
peak_multiplier = 1.25 # peak season: 5/15-8/15 & 12/15-1/15
weekend_surcharge = 30  #weekends are $30 more than base price (applied after peak mult)