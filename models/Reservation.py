
from .Client import Client
from dateutil import parser
import datetime

#Static HOTEL variables - base prices are weekday, off-season
hotel_baseprice = {'Single': 140, 'Double': 260, 'Quad': 480}
peak_multiplier = 1.25 # peak season: 5/15-8/15 & 12/15-1/15
weekend_surcharge = 30  #weekends are $30 more than base price (applied after peak mult)

class Reservation:

    ID = 20000

    def __init__(self, clientID, checkinDate, checkoutDate, num_guests):
        self.ID = Reservation.ID
        Reservation.ID += 1
        self.clientID = clientID
        self.checkin = checkinDate
        self.checkout = checkoutDate
        self.num_guests = num_guests
        self.checked_in = False
        self.checked_out = False
        [self.nights,self.nightly_rates,self.ttlcost] = self.calc_cost()
    
    def __str__(self):
        return "Reservation (%s, %s): #%d for client %d from %s to %s with %d guest(s) - $%d" % \
            ("checked in" if self.checked_in else "not checked in",
            "checked out" if self.checked_out else "not checked out", self.ID, self.clientID,
            self.checkin, self.checkout, self.num_guests, self.ttlcost)

    def calc_cost(self):
        #calc the base price based on occupancy
        if self.num_guests == 1:
            base_price = hotel_baseprice['Single']
        elif self.num_guests == 2:
            base_price = hotel_baseprice['Double']
        elif 3 <= self.num_guests <= 4:
            base_price = hotel_baseprice['Quad']
        else:
            raise AttributeError()
        #adjust base price for peak and weekends
        # peak season: 5/15-8/15 & 12/15-1/15
        [check_in, check_out] = [parser.parse(self.checkin), parser.parse(self.checkout)]
        num_nights = (check_out-check_in).days
        nightly_prices = [base_price for q in range(0,num_nights)]
        date_list = [check_in + datetime.timedelta(days=q) for q in range(0,num_nights)]
        for i in range(0,len(date_list)):
            year = date_list[i].year
            if date_list[i] <= datetime.datetime(year, 1, 15):
                nightly_prices[i] *= peak_multiplier
            elif datetime.datetime(year, 5, 15) <= date_list[i] <= datetime.datetime(year, 8, 15):
                nightly_prices[i] *= peak_multiplier
            elif date_list[i] >= datetime.datetime(year, 12, 15):
                nightly_prices[i] *= peak_multiplier
            if date_list[i].weekday() == 5 or date_list[i].weekday() == 6:
                nightly_prices[i] += weekend_surcharge
        return [date_list,nightly_prices,sum(nightly_prices)]

