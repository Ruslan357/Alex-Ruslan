def is_palindrome(text):
    return text[0:int(len(text)/2)] == text[-1:int(len(text)/2):-1]
    
print(is_palindrome('redivider'))
