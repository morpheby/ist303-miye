class SpaRes:
  
  def __init__(self, personID, date, time, treatment_type, duration):
    self.person = personID
    self.date = date
    self.time = time
    self.treatment_type = treatment_type
    self.duration = duration

  def checkSpaAvailability(date, time, type):
    pass

  def makeSpaRes(clientID, date, time, treatment_type):
    SpaRes(clientID, date, time, treatment_type)

  def print_avail_sched():
    pass

  def print_price_menu():
    pass


#SPA STATIC VARS
#available time slots
timeslots_military = [(x + 5)/10 for x in range(75,200,5)]
timeslots = [] #human readable list of time slots, i.e. 3:00 PM instead of 14
for timeval in timeslots_military:
  hour_min = divmod(timeval,1)
  if timeval < 12:
    ampm = 'AM'
    hour = int(hour_min[0])
  elif timeval == 12 or timeval == 12.5:
    ampm = 'PM'
    hour = int(hour_min[0])
  else:
    ampm = 'PM'
    hour = int(hour_min[0]-12)
  min = int(hour_min[1]*60)
  min = str(min)
  if min == '0':
    min = '00'
  timeslots.append(str(hour) + ":" + min + " " + ampm)



