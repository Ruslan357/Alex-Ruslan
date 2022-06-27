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
