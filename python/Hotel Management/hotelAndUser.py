class Hotel:
    sortParam = 'name'

    def __init__( self ) -> None:
        self.name = ''
        self.roomAvl = 0
        self.location = ''
        self.rating = int
        self.pricePr = float
    
    def __lt__( self, other ):
        getattr( self, Hotel.sortParam ) < getattr( other, Hotel.sortParam )

    
    @classmethod
    def sortByName( cls ):
        cls.sortParam='name'
    
    @classmethod
    def sortByRate( cls ):
        cls.sortParam='rating'

    @classmethod
    def sortByRoomAvailable( cls ):
        cls.sortParam='roomAvl'

    def __repr__( self ) -> str:
        return f"PRHOTELS DATA:\nHotelName:{self.name}\tRoom Available:{self.roomAvl}\tLocation:{self.location}\tRating:{self.rating}\tPrice Per Room:{self.pricePr}"
    
class User:
    def __init__( self ) -> None:
        self.uname = ''
        self.uid = ''
        self.cost = ''

    def __repr__( self ) -> str:
        return f"UserName:{self.uname}\tUserId:{self.uid}\tBooking Cost:{self.cost}"
    

def PrintHotelData( hotels ):
    for h in hotels:
        print(h)


def SortHotelByName( hotels ):
    print("SORT BY NAME:")

    Hotel.sortByName()
    hotels.sort()

    PrintHotelData( hotels )
    print()


def SortHotelByRating( hotels ):
    print("SORT BY RATING:")

    Hotel.sortByRate()
    hotels.sort()

    PrintHotelData( hotels )
    print()


def SortHotelByCity( location, hotels ):
    print(f"HOTELS FOR {location} LOCATION ARE:")
    hotelsByLoc = [h for h in hotels if h.location == location]

    PrintHotelData( hotelsByLoc )
    print()


def SortHotelByRoomAvailable( hotels ):
    print("SORT BY ROOM AVAILABLE:")

    Hotel.sortByRoomAvailable()
    hotels.sort()

    PrintHotelData( hotels )
    print()


def PrintUserData( userName, userId, bookingCost, hotels ):
    users = []

    for i in range(3):
        u=User()
        u.uname = userName
        u.uid = userId
        u.cost = bookingCost
        users.append(u)
    
    for i in range(len(users)):
        print(users[i], f"\tHotel Name:{hotels}")