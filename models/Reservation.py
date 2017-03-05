
from .Client import Client

class Reservation:

  ID = 20000

  #do we need reservation ID
  def __init__(self, clientID, checkinDate, checkoutDate, num_guests):
    self.ID = Reservation.ID
    Reservation.ID += 1
    self.clientID = clientID
    self.checkin = checkinDate
    self.checkout = checkoutDate
    self.num_guests = num_guests
    self.checked_in = False
    self.checked_out = False
    
    def __str__(self):
        return "Reservation (%s, %s): #%d for client %d from %s to %s with %d guest(s)" % \
            ("checked in" if self.checked_in else "not checked in",
            "checked out" if self.checked_out else "not checked out", self.ID, self.clientID,
            self.checkin, self.checkout, self.num_guests)
