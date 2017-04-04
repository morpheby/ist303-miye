
from .Client import Client
import datetime
import support.exceptions as exc
from support import parse_date_or_not
from .CostUnit import CostUnit, CostMultiply, CostAdd, CostList, TotalTraverser

#Static HOTEL variables - base prices are weekday, off-season
PEAK_MULTIPLIER = 1.25 # peak season: 5/15-8/15 & 12/15-1/15
WEEKEND_SURCHARGE = 30  #weekends are $30 more than base price (applied after peak mult)

class Reservation(object):

    ID = 20000

    def __init__(self, clientID, checkinDate, checkoutDate, roomID, guest_ids):
        super(Reservation, self).__init__()
        
        self.ID = Reservation.ID
        Reservation.ID += 1
        self.clientID = clientID
        self.roomID = roomID
        self.guest_ids = guest_ids
        self.checked_in = False
        self.checked_out = False
        
        self._checkin = None
        self._checkout = None

        self.checkin = checkinDate
        self.checkout = checkoutDate
        
        self.build_cost()
    
    def __str__(self):
        checkedin = "checked in" if self.checked_in else "not checked in"
        checkedout = "checked out" if self.checked_out else "not checked out"
        guests = ', '.join([str(g) for g in self.guest_list])
        return f"Reservation ({checkedin}, {checkedout}): #{self.ID} for client {self.client}" \
            f" with guests [{guests}] in room {self.room} from {self.checkin} to" \
            f" {self.checkout} ({self.nights}) - ${self.total_cost}"

    @property
    def nights(self):
        "Count of nights"
        return (self.checkout - self.checkin).days

    def build_cost(self):
        """
        Builds CostBase objects chain for cost calculation
        """
        nightly_prices = []
        date_list = [self.checkin + datetime.timedelta(days=q) for q in range(0, self.nights)]
        for date in date_list:
            year = date.year
            price = self.room.price
            if date <= datetime.datetime(year, 1, 15):
                price = CostMultiply(price, PEAK_MULTIPLIER, "Peak season 12/15 - 1/15")
            elif datetime.datetime(year, 5, 15) <= date and date <= datetime.datetime(year, 8, 15):
                price = CostMultiply(price, PEAK_MULTIPLIER, "Peak season 5/15 - 8/15")
            elif date >= datetime.datetime(year, 12, 15):
                price = CostMultiply(price, PEAK_MULTIPLIER, "Peak season 12/15 - 1/15")
            
            if date.weekday() == 5 or date.weekday() == 6:
                price = CostAdd(price, WEEKEND_SURCHARGE, "Weekend surcharge")
                
            nightly_prices += [price]
            
        self.cost = CostList(nightly_prices, f"Cost for reservation #{self.ID}")

    @property
    def total_cost(self):
        """Total cost of the reservation"""
        return TotalTraverser(self.cost)()

    @property
    def checkin(self):
        "Date of checkin"
        return self._checkin
    
    @checkin.setter
    def checkin(self, value):
        self._checkin = parse_date_or_not(value)
        
    @checkin.deleter
    def checkin(self):
        del self._checkin   

    @property
    def checkout(self):
        "Date of checkout"
        return self._checkout
    
    @checkout.setter
    def checkout(self, value):
        self._checkout = parse_date_or_not(value)
        
    @checkout.deleter
    def checkout(self):
        del self._checkout

