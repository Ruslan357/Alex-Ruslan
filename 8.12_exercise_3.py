def is_palindrome(text):
    if text[0:int(len(text)/2)] == text[-1:int(len(text)/2):-1]:
        return True
    return False
    
print(is_palindrome('redivider'))
