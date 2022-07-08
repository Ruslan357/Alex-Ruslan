def gcd(a,b):
    while a!=b:
        if a>b:
            a-=b
        else:
            b-=a
        gcd(a,b)
    return a

print(gcd(54,24))
