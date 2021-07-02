# ************* RNewrealtor.py ***************** #
from realtor import Realtor
class Newrealtor(Realtor):
    def __init__(self, zipcode, pptyId, price):
        Realtor.__init__(self,zipcode,pptyId)
        self.__inventory1 = {2110:495000.00, 2115:489000.00}
        self.__inventory2 = {3260:624000.00, 3266:599000.00}
        self. __price = price
    def setprice(self,newprice):
        self.__price = newprice
    def getprice(self):
        return self.__price
    def getinventory(self):
        if self.getzip() == 11322:
            return self.__inventory1
        else:
            return self.__inventory2  

