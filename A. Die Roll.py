import math

def min_probability(y, w):
    max_value = max(y, w)
    outcomes = 6 - max_value + 1
    gcd = math.gcd(outcomes, 6)
    return f"{outcomes // gcd}/{6 // gcd}"
    
y, w =map(int, input().split())
print(min_probability(y, w))
