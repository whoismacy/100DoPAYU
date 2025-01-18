"Prime Numbers"
import math

def is_prime(n1):
    if n1 == 2:
        return True
    if n1 == 0 or n1 == 1:
        return False
    if n1 % 2 == 0:
        return False
    # The Smallest factor in each pair is always less than
    # Or equal to the squareroot
    for i in range(3, (int(math.sqrt(n1)) + 1), 2):
        if n1 % i == 0:
            return False
    return True
