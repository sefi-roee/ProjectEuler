# -------------------------------------------------------------- Ordered radicals ----------------------------------------------------------------- #
#                                                                                                                                                   #
#       The radical of n, rad(n), is the product of the distinct prime factors of n. For example, 504 = 23 × 32 × 7, so rad(504) = 2 × 3 × 7 = 42.  #
#                                                                                                                                                   #
#       If we calculate rad(n) for 1 ≤ n ≤ 10, then sort them on rad(n), and sorting on n if the radical values are equal, we get:                  #
#                                                                                                                                                   #
#                                                           Unsorted                        Sorted                                                  #
#                                                           n   rad(n)                      n   rad(n)  k                                           #
#                                                           1   1                           1   1       1                                           #
#                                                           2   2                           2   2       2                                           #
#                                                           3   3                           4   2       3                                           #
#                                                           4   2                           8   2       4                                           #
#                                                           5   5                           3   3       5                                           #
#                                                           6   6                           9   3       6                                           #
#                                                           7   7                           5   5       7                                           #
#                                                           8   2                           6   6       8                                           #
#                                                           9   3                           7   7       9                                           #
#                                                           10  10                          10  10      10                                          #
#                                                                                                                                                   #
#       Let E(k) be the kth element in the sorted n column; for example, E(4) = 8 and E(6) = 9.                                                     #
#                                                                                                                                                   #
#       If rad(n) is sorted for 1 ≤ n ≤ 100000, find E(10000).                                                                                      #
# ------------------------------------------------------------------------------------------------------------------------------------------------- #
import time
from euler.numbers import get_distinct_factors
from operator import mul
from functools import reduce

def radical(n):
    f = get_distinct_factors(n)

    return reduce(mul, f)

def eu124():
    TOP = 100000
    TARGET = 10000

    l = [(1, 1)]
    
    for i in range(2, TOP + 1):
        l.append((radical(i), i))

    l = sorted(l)
    
    return l[TARGET - 1][1]

if __name__ == "__main__":
    startTime = time.clock()
    print (eu124())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
