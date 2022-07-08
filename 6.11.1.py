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
