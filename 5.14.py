        # Exercise 1
import time
start = int(time.time())

hours = start//3600
minutes = (start - (hours * 3600))//60
seconds = (start - (hours * 3600)) - (minutes*60)
days = start//3600//24
hours_in_time = int(((start//3600/24)-(start//3600//24))*24)

print(f'\nDays have passed: {days}')
print(f'Time: {hours_in_time:02}:{minutes:02}:{seconds:02} (UTC)\n')
        
        # Exercise 2
#2.1
def check_fermat(a,b,c,n):
    if n > 2 and  a**n + b**n == c**n:
        print("Holy smokes, Fermat was wrong!\n")
    else:
        print("No, that doesn’t work.\n")

#2.2
def conversion():
    a=int(input("Enter a\n"))
    b=int(input("Enter b\n"))
    c=int(input("Enter c\n"))
    n=int(input("Enter n\n"))
    check_fermat(a,b,c,n)

conversion()

        # Exercise 3
#3.1
def is_triangle(segment_1, segment_2, segment_3):
    if segment_1>segment_2+segment_3 or segment_2>segment_1+segment_3 or segment_3>segment_1+segment_2:
        print("No\n")
    else:
        print("Yes\n")

#3.2
def conversion():
    seg_1=int(input("Enter segment 1\n"))
    seg_2=int(input("Enter segment 2\n"))
    seg_3=int(input("Enter segment 3\n"))
    is_triangle(seg_1, seg_2, seg_3)

conversion()

is_triangle(12,1,1)

        # Exercise 4

# 4.1  Answer: the program will give an error due to exceeding the allowed number of recursions (infinite recursion)

# 4.2
def recurse(n, s):
    """ n,s - variables that change their values during a recursive function call. 
        The function outputs the value of c when the value of n reaches 0
    """
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

recurse(3, 0)
