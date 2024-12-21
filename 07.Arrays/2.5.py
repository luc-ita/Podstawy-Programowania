# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

def seats_total(seats):
   total = 0
   for i in seats:
      for j in i:
         total += 1
   return total

def seats_available(seats):
   free = 0
   for i in seats:
      for j in i:
         if j == 'A':
            free += 1
   return free

def seats_booked(seats):
   busy = 0
   for i in seats:
      for j in i:
         if j == 'B':
            busy += 1
   return busy

def seat_status(seats, row, place):
   status = seats[row-1][place-1]
   return status

print('CINEMA INFORMATION TABLE')
print('Total seats:',seats_total(cinema_seats))
print('Seats available:', seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats,1,1))
print('Seat in row 5, place 5:', seat_status(cinema_seats,5,5))
print('Seat in row 3, place 5:', seat_status(cinema_seats,3,5))