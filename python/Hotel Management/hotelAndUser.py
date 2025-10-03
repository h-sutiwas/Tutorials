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
        return f"{self.name}\t{self.roomAvl}\t{self.location}\t{self.rating}\t{self.pricePr}"
    
class User:
    def __init__( self ) -> None:
        self.uname = ''
        self.uid = 0
        self.cost = 0

    def __repr__( self ) -> str:
        return f"{self.uname}\t{self.uid}\t{self.cost}"
    

def PrintHotelData( hotels ):
    print("PRINT HOTELS DATA")
    print("HotelName\tRoom Available\tLocation\tRating\tPrice Per Room")
    for h in hotels:
        print(h)


def SortHotelByName( hotels ):
    print("SORT BY NAME:")

    Hotel.sortByName()
    hotels.sort()

    PrintHotelData( hotels )
    print()


def SortHotelByRating( hotels ):
    print("SORT BY A RATING:")

    Hotel.sortByRate()
    hotels.sort()

    PrintHotelData( hotels )
    print()


def PrintHotelByCity( location, hotels ):
    print("HOTELS FOR {} LOCATION ARE:".format(location))
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
    print("PRINT USER BOOKING DATA:")
    print("UserName\tUserId\tBooking Cost\tHotelName")

    users = []

    for i in range(3):
        u=User()
        u.uname = userName[i]
        u.uid = userId[i]
        u.cost = bookingCost[i]
        users.append(u)
    
    for i in range(len(users)):
        print(users[i], "\t", hotels[i].name)