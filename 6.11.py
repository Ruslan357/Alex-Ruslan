                #Exercise 2
def ack(m,n):
    if m==0:
        return n+1
    elif m>0 and n==0:
        return ack(m-1, 1)
    elif m>0 and n>0:
        return ack(m-1, ack(m,n-1))

print(ack(3,4))

'''
for values large m and n, an excessively large number of recursive function ack()
calls occur, which leads to an error (maximum recursion depth exceeded in comparison).
'''

                #Exercise 3

                # 3.1

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

print(middle(''))

'''
What happens if you call middle with a string with two letters? One letter?
What about the empty string, which is written and contains no letters?

Answer: text is out of range
'''

# 3.2
def is_palindrome(text):
    for i in range(0,int(len(text)/2)):
        if text[i]!=text[len(text)-i-1]:
            return False
    return True

print(is_palindrome('redivider'))

                #Exercise 4

def is_power(a, b):
    while a % b == 0:
        if a == b: 
            return True
        a /= b
    return False

print(is_power(6, 2))
print(is_power(8, 2))

                #Exercise 5
def gcd(a,b):
    while a!=b:
        if a>b:
            a-=b
        else:
            b-=a
        gcd(a,b)
    return a

print(gcd(54,24))
