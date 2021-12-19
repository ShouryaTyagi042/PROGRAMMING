import math
import random
rng = random.Random()

def share_diagonal(x0, y0, x1, y1):
    """ Is (x0, y0) on a shared diagonal with (x1, y1)? """
    dy = abs(y1 - y0)        # Calc the absolute y distance
    dx = abs(x1 - x0)        # CXalc the absolute x distance
    return dx == dy          # They clash if dx == dy
def col_clashes(bs, c):
    """ Return True if the queen at column c clashes
         with any queen to its left.
    """
    for i in range(c):     # Look at all columns to the left of c
          if share_diagonal(i, bs[i], c, bs[c]):
              return True

    return False           # No clashes - col c has a safe placement.
def has_clashes(the_board):
    """ Determine whether we have any queens clashing on the diagonals.
        We're assuming here that the_board is a permutation of column
        numbers, so we're not explicitly checking row or column clashes.
    """
    for col in range(1,len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False
def main():
   # Instantiate a generator
    bd = list(range(8))     # Generate the initial permutation
    num_found = 0
    tries = 0
    while num_found < 10:
       rng.shuffle(bd)
       tries += 1
       if not has_clashes(bd):
           print("Found solution {0} in {1} tries.".format(bd, tries))
           tries = 0
           num_found += 1
l = list(range(1,50))
def lotto() :
    lotto = random.sample(l,6)
    return lotto
# print(lotto())
l1 = lotto()
key = [2,8,40,47,15,34]
def lotto_match(l1,l2) :
    l1.sort()
    l2.sort()
    xi = 0
    yi =0
    result = []
    while True :
        if xi >= 6 or yi >= 6 :
            break
        elif l1[xi] < l2[yi] :
            xi += 1
        elif l1[xi] > l2[yi] :
            yi += 1
        else :
            result.append(l1[xi])
            xi += 1
    return result
# print(lotto_match(l1,key))
def is_prime(s) :
    flag = True
    if s == 1 :
        flag = False
    else :
        end = math.ceil(math.sqrt(s))
        for i in range(2,end+1) :
            if s%i == 0 :
                flag = False
                break
        return flag
# print(is_prime(4))

def primes_in(l1) :
    ans = 0
    for num in l1 :
        if is_prime(num) == True :
            ans += 1
    return ans
# print(primes_in([42, 4, 7, 11, 1, 13]))







