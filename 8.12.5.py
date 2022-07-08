def rotate_word(s,num):
    new_s = '' 
    for i in s:
        new_s+=chr(ord(i)+num)
    return new_s

print(rotate_word('abc',2))
