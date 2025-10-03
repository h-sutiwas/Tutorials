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