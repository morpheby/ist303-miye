
from .Room import Room
from .Client import Client
from .Reservation import Reservation
from support import Singleton

@Singleton
class Repository(object):
    
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
            
    def find_reservations_checked(self, c_in, c_out):
        found = [r for r in self.reservations if r.checked_in == c_in and r.checked_out == c_out]
        return found
