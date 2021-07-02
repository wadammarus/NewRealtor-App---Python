# ************* testnewrealtor.py ***************** #
from newrealtor import Newrealtor

def main():
    done = False
    while not done:
        zipcode = int(input('Please choose your zip code {11322, 11333}: '))
        if zipcode != 11322 and zipcode != 11333:
            print('You have to choose one from the list, please try again !!')
        else:
            done = True 

    done = False
    pptyId = 0
    price = 0
    realstate = Newrealtor(zipcode,pptyId,price)
    inventory = realstate.getinventory()
    keys = set()
    for x in inventory.keys():
        keys.add(x)
    while not done:
        pptyId = int(input("Please choose from these propertiy id's available in your zip code " + str(keys) + ': ' ))
        if pptyId not in keys:
            print("You have to choose from the list of id's available , plesae try agian !!")
        else:
            done = True

    realstate.setpptyId(pptyId)
    realstate.setprice(inventory[pptyId]) 
    
    done = False
    while not done:
        sqft = float(input("Please enter the square feet of this properity : "))
        if sqft <= 0 :
            print('Please enter real numbers , you can try again !!')
        else:
            done = True
    done = False
    while not done:
        bed = int(input("Please enter the number of bedrooms : "))
        if bed <= 0 :
            print('Please enter real numbers , you can try again !!')
        else:
            done = True                
    done = False
    while not done:
        bath = int(input("Please enter the number of bathrooms : "))
        if bath <= 0 :
            print('Please enter real numbers , you can try again !!')
        else:
            done = True    
    realstate.setsqft(sqft)
    realstate.setbed(bed)
    realstate.setbath(bath)      
    done = False
    while not done:
        availability = str(input("do you want to make this properity avialable (Y,N)?  ")).lower()
        if availability != 'y' and availability != 'n' :
            print('Please choose (Y/N) , you can try again !!')
        else:
            if availability == 'y':
                realstate.setAvailability(True)
            done = True    

    print('*********************************************************************') 
    print('*                 Real Estates in zip code                          *') 
    print('*                           ( '+ str(zipcode) +' )                               *') 
    print('*********************************************************************\n') 

    print('Zip Code:       ',realstate.getzip())
    print('Property Id:    ',realstate.getpptyId())
    print('Square Feets:   ',realstate.getsqft())
    print('Number of Beds: ',realstate.getbed())
    print('Number of Baths:',realstate.getbath())
    print('Price:          ','$'+str (realstate.getprice()))
    print('Property Tax:   ','$%.2f' % realstate.pptyTax())
    print('Available:     ','(',realstate.isAvailable(),')\n')
     

main()            







