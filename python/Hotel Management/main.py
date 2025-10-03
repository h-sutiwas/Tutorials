from hotelAndUser import *



def HotelManagement(userName, userId, hotelName,
                     bookingCost, rooms, locations,
                     ratings, prices):
    hotels = []

    for i in range(3):
        h=Hotel()
        h.name = hotelName[i]
        h.roomAvl = rooms[i]
        h.location = locations[i]
        h.rating = ratings[i]
        h.pricePr = prices[i]

        hotels.append(h)

    print()

    PrintHotelData(hotels)
    SortHotelByName(hotels)
    SortHotelByRating(hotels)
    PrintHotelByCity("Bangalore",
                     hotels)
    SortHotelByRoomAvailable(hotels)
    PrintUserData(userName,
                  userId,
                  bookingCost,
                  hotels)

if __name__ == '__main__':
    userName = ["U1", "U2", "U3"]
    userId = [2, 3, 4] 
    hotelName = ["H1", "H2", "H3"] 
    bookingCost = [1000, 1200, 1100]
    rooms = [4, 5, 6] 
    locations = ["Bangalore",
                           "Bangalore",
                           "Mumbai"]
    ratings = [5, 5, 3]
    prices = [100, 200, 100] 

    HotelManagement(userName, userId,
                    hotelName, bookingCost,
                    rooms, locations,
                    ratings, prices)