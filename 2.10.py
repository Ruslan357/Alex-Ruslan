import math
from decimal import Decimal   
    #Exercise 2.1

radius = 5
volume_of_sphere = 4/3 * math.pi * radius**3
print(f'The volume of the ball is equal to {volume_of_sphere}\n')

    #Exercise 2.2
price = 24.95
discount = 0.4
delivery_firs = 3
delivery_after = 0.75
number_of_books = 60

total = (number_of_books * (price - (price * discount))) + (delivery_after * (number_of_books - 1)) + delivery_firs
answer = Decimal(str(total))
print(f'The purchase price of 60 books with delivery is = {answer.quantize(Decimal("1.00"))} $\n')

    #Exercise 2.3
              
slow_pace = 8*60+15 
fast_pace = 7*60+12
start = 24720                                     #6:52 is 24,720 seconds from the start of the day
total = start + 2* slow_pace + 3 * fast_pace       
hours = total//3600
minutes = (total - (hours * 3600))//60
seconds = (total - (hours * 3600)) - (minutes*60)

print(f'I will return home at {hours:02}:{minutes:02}:{seconds:02}\n')
