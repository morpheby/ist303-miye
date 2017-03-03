
import .Client

class Reservation:

  #do we need reservation ID
  def __init__(self, clientID, creditcard, checkinDate, checkoutDate, num_guests):
    self.clientID = clientID
    self.checkin = checkinDate
    self.checkout = checkoutDate
    self.num_guests = num_guests
    self.checked_in = 0
    Client.addcard(self.clientID, creditcard)

  def checkHotelAvailability(checkinDate, checkoutDate, num_guests):
    pass

  def makeRes(clientID, creditcard, checkinDate, checkoutDate, num_guests):
    Reservation(clientID, creditcard, checkinDate, checkoutDate, num_guests)

  def Input_client_data():
    pass
