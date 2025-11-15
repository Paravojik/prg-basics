cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]
def seats_total(seats):
    total=0
    for i in seats:
        total+=len(i)
    return total
def seats_booked(seats):
    total=0
    for i in seats:
        for j in i:
            if j=="B":
                total+=1
    return total

def seat_status(seats, row, place):
    if seats[row][place]=="B":
        return "Booked"
    else:
        return "Available"
    
print('CINEMA INFORMATION TABLE')
print('Total seats:',seats_total(cinema_seats))
print('Seats available:',seats_total(cinema_seats) - seats_booked(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats, 0, 0))
print('Seat in row 5, place 5:', seat_status(cinema_seats, 4, 4))
print('Seat in row 3, place 5:', seat_status(cinema_seats, 2, 4))