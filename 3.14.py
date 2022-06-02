                #Exercise 1 

def right_justify(s):
    while len(s)!=70:
        s=' '+s
    print(s)

right_justify('hello')


                #Exercise 2.1 

def do_twice(f):
    f()
    f()

def print_spam():
    print('spam')

do_twice(print_spam)

# 2.2 
def do_twice(f,s):
    f(s)
    f(s)

def print_spam(s):
    print(s + 'spam')

do_twice(print_spam, 'this is ')

# 2.3 
def do_twice(f,s):
    f(s)
    f(s)

def print_twice(s):
    print(s + 'spam')
    print(s + 'spam')

do_twice(print_twice, 'this is ')


# 2.4 
def do_twice(f,s):
    f(s)
    f(s)

def print_twice(s):
    print(s + 'spam')
    print(s + 'spam')

do_twice(print_twice, 'spam ')

# 2.5 (final)
def do_four(f,s):
    for i in range(3):
        f(s)  

def print_twice(s):
    print(s + 'spam')
    print(s + 'spam')

do_four(print_twice, 'spam ')

                #Exercise 3
# 3.1

def square_part1():
    print('+', '- ' * 4 + '+', '- ' * 4 + '+')

def square_part2():
    print('|', ' ' * 8 + '|', ' ' * 8 + '|')

def square_part3():
    print('+', '- ' * 4 + '|', '- ' * 4 + '+')
    
def square():
    square_part1()
    for i in range(4):
        square_part2()
    square_part3()
    for i in range(4):
        square_part2()
    square_part1()
   
square()

