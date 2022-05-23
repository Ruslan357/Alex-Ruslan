#Exercise 2.1
answer1 = 42*60+42
print(f'There are {answer1} seconds in 42 minutes 42 seconds\n')

#Exercise 2.2
answer2  = 10/1.61
print (f'There are {answer2} miles in 10 kilometers\n')

#Exercise 2.3
distance_km=10
time=42.42
distance_mile = distance_km/1.61
average_pace_per_min = distance_mile/time
average_pace_per_sec = average_pace_per_min/60
average_speed_per_hour = average_pace_per_min*60

print(f'The average pace {average_pace_per_min} per mile/minutes\n')
print(f'The average pace {average_pace_per_sec} per mile/seconds\n')
print(f'The average speed is {average_speed_per_hour} miles/hour\n')
