# https://www.codewars.com/kata/56269eb78ad2e4ced1000013/python

import math
def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    print(sq)
    if(sq%math.sqrt(sq) == 0):
        nexts = (math.sqrt(sq)+1)
        return nexts*nexts
    return -1
