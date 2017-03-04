
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
    self.checked_in = 0
