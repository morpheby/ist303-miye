
class Reservation:
  
  # base prices are weekday, off-season
  hotel_baseprice = {'Single': 140,
  'Double': 260,
  'Quad': 480}
  
  peak_multiplier = 1.25 # peak season: 5/15-8/15 & 12/15-1/15
  weekend_surcharge = 30

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
