import math

def is_perfect_square(n):
    if math.sqrt(n).is_integer():
        return True
    return False