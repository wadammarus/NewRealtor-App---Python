# ************* Realtor.py ***************** #
class Realtor:
    def __init__(self, zipcode, pptyId):
        self.__zip    = zipcode
        self.__pptyId = pptyId
        self.__sqft   = 0
        self.__bed    = 0
        self.__bath   = 0
        self.__isAvailable = False
    def setpptyId(self, newpptyId):
        self.__pptyId = newpptyId
    def setzip(self, newzipcode):
        self.__zip = newzipcode
    def setsqft(self, newsqft):
        self.__sqft = newsqft
    def setbed(self, newbed):
        self.__bed = newbed
    def setbath(self, newbath):
        self.__bath = newbath
    def setAvailability(self, status):
        if status == True:
            self.__isAvailable =  True   
    def getpptyId(self):
        return self.__pptyId
    def getzip(self):
        return self.__zip
    def getsqft(self):
        return self.__sqft
    def getbed(self):
        return self.__bed
    def getbath(self):
        return self.__bath
    def isAvailable(self):
        return self.__isAvailable
    def pptyTax(self):
        if self.__zip == 11322:
            return  float((self.__sqft * (3.05/100) ) + (self.__bed * 150) + (self.__bath * 100 ))
        elif self.__zip == 11333:
            return  float((self.__sqft * (3.15/100) ) + (self.__bed * 150) + (self.__bath * 100 ))
        else:
            return 0







