
from .Room import Room
from .Client import Client
from .Reservation import Reservation
from support import Singleton
from .ReservationSearcher import ReservationSearcher

@Singleton
class Repository(object):
    
    def __init__(self):
        self.rooms = []
        self.clients = []
        self.reservations = []
        self.res_srchr = ReservationSearcher(self.reservations)
        
    def post_init(self):
        #create the master list of all rooms: [room #, max occ.]
        single = [ [101 + x, 1] for x in range(16) ]
        double = [ [201 + x, 2] for x in range(16) ]
        quad = [ [301 + x, 4] for x in range(4) ]
        self.rooms = [Room(r,g) for r,g in single + double + quad]

        self.clients = [Client(*name.split(' ')) for name in ['Test User', "Another One", "Third Also"]]
        self.reservations = [Reservation(self.clients[i].ID, f"{i+1}/1/2005", f"{i+1}/20/2005", self.rooms[i].ID, [self.clients[i].ID]) for i in range(len(self.clients))]
        
        # After loading reservations, it is best to rebuild ReservationSearcher
        self.res_srchr = ReservationSearcher(self.reservations)

    def add_client(self, client):
        self.clients += [client]
    
    def add_reservation(self, reservation):
        self.reservations += [reservation]
        self.res_srchr.add_reservation(reservation)
    
    def find_client_by_id(self, clientID):
        found = [c for c in self.clients if c.ID == clientID]
        if len(found) == 0:
            return None
        else:
            return found[0]
    
    def find_room_by_id(self, roomID):
        found = [r for r in self.rooms if r.ID == roomID]
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
            
    def delete_object(self, obj):
        if type(obj) == Room:
            self.rooms = [r for r in self.rooms if r.ID != obj.ID]
        elif type(obj) == Client:
            self.clients = [r for r in self.clients if r.ID != obj.ID]
        elif type(obj) == Reservation:
            self.reservations = [r for r in self.reservations if r.ID != obj.ID]
        else:
            raise InputError
        
            
    def find_reservations_checked(self, c_in, c_out):
        found = [r for r in self.reservations if r.checked_in == c_in and r.checked_out == c_out]
        return found
        
    def find_free_rooms_in_dates(self, date_start, date_end):
        occupied = self.res_srchr.get_occupied_rooms(date_start, date_end)
        return [r for r in self.rooms if r.ID not in occupied]
