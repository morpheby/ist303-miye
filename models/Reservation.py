
class Reservation:
  
  # base prices are weekday, off-season
  hotel_baseprice = {'Single': 140,
  'Double': 260,
  'Quad': 480}
  
  peak_multiplier = 1.25 # peak season: 5/15-8/15 & 12/15-1/15
  weekend_surcharge = 30

  def checkHotelAvailability(self, date, occ):
    pass

  def makeReservation(self, date, occ, ID):
    Reservation.checkHotelAvailability()