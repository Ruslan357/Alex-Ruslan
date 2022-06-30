def any_lowercase1(s):
    '''
        Detects whether a string contains lowercase letters and returns a bool value
    '''
    for c in s:
        if c.islower():
            return True
        else:
            return False

            

def any_lowercase2(s):
    '''
        Returns True value because the letter 'c' islower
    '''
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'




def any_lowercase3(s):
    '''
        Returns True value if the last letter in a word is lower
    '''
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    '''
        Returns True value if the last letter in a word is lower
    '''
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag



def any_lowercase5(s):
    '''
        Returns True value if the first letter in a word is lower
    '''
    for c in s:
        if not c.islower():
            return False
    return True


