class SpaRes:

  def __init__(self, personID, date, time, treatment_type):
    self.person = personID
    self.date = date
    self.time = time
    self.treatment_type = treatment_type

  def checkSpaAvailability(date, time, type):
    pass

  def makeSpaRes(clientID, date, time, treatment_type):
    SpaRes(clientID, date, time, treatment_type)

  def print_avail_sched():
    pass

  def print_price_menu():
    pass

