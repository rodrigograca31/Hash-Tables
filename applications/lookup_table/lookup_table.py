import time
import math
import random

cache = {}


def slowfun(x, y):

    if str(x)+"_"+str(y) in cache.keys():
        return cache[str(x)+"_"+str(y)]
    # TODO: Modify to produce the same results, but much faster
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653
    cache[str(x)+"_"+str(y)] = v
    return v


# Do not modify below this line!

start = time.time()

for i in range(100000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')

print("Imp 1: \t%.8f" % float(time.time() - start))
