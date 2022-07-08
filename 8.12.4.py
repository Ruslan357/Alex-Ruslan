def any_lowercase1(s):
    '''
        Determines whether the first letter of a string is lowercase and returns a Boolean value
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
        Returns the last letter of a string as a lowercase letter
    '''
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    '''
        Returns False value 
    '''
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag



def any_lowercase5(s):
    '''
        Returns False if the string contains an uppercase letter
    '''
    for c in s:
        if not c.islower():
            return False
    return True


