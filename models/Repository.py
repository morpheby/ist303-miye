
class Repository(object):
    __instance = None
    
    def __new__(cls, *args, **kwargs):
        if Repository.__instance is None:
            Repository.__instance = object.__new__(cls, *args, **kwargs)
        return Repository.__instance

    def __init__(self, preload=None):
        self._repos = {}
        if preload:
            self._repos.update(preload)

    def register(self, name, repo):
        self._repos[name] = repo

    def get(self, name):
        return self._repos[name]


#Static HOTEL variables
# base prices are weekday, off-season
hotel_baseprice = {'Single': 140, 'Double': 260, 'Quad': 480}
peak_multiplier = 1.25 # peak season: 5/15-8/15 & 12/15-1/15
weekend_surcharge = 30  #weekends are $30 more than base price (applied after peak mult)