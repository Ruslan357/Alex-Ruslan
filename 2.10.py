import math   
    #Exercise 2.1

radius = 5
volume_of_sphere = 4/3 * math.pi * radius
print(f'The volume of the ball is equal to {round(volume_of_sphere,2)}\n')

    #Exercise 2.2
price = 24.95
discount = 0.4
delivery_firs = 3
delivery_after = 0.75
number_of_books = 60

total = number_of_books * ((price - (price*discount))) - (delivery_after * (number_of_books - 1) - delivery_firs)

print(f'The purchase price of 60 books with delivery is = {round(total,3)}$\n')

    #Exercise 2.3
start = (6 * 60 + 52) / 60
round1 = (8 * 60 + 15) / 60
round2 = 3 * ((7 * 60 + 12)) / 60
round3 = round1
time_of_run = round1 + round2 + round3

print(f'I will return home in {time_of_run} minutes\n')