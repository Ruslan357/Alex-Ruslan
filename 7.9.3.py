import math

def estimate_pi():
    temp = 1
    k = 0
    sum = 0
    while temp >= 10**-15:
        sum += (math.factorial(4*k) * (1103 + 26390*k)) / (math.factorial(k)**4 * 396**(4*k))
        temp = (2*math.sqrt(2))/9801 * (math.factorial(4*k) * (1103 + 26390*k)) / (math.factorial(k)**4 * 396**(4*k))
        k += 1
    return 1 / ((2*math.sqrt(2))/9801 * sum)

print(estimate_pi())
