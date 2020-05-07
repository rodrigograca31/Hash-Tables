import time
cache = {}


def expensive_seq(x, y, z):
    # Implement me

    # use a tuple as the Key
    if (x, y, z) in cache.keys():
        return cache[(x, y, z)]

    result = None
    if x <= 0:
        result = y + z
    if x > 0:
        result = expensive_seq(
            x-1, y+1, z) + expensive_seq(x-2, y+2, z*2) + expensive_seq(x-3, y+3, z*3)

    # use a tuple as the Key
    cache[(x, y, z)] = result
    return result


if __name__ == "__main__":
    start = time.time()

    for i in range(100):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
    print("Imp 1: \t%.8f" % float(time.time() - start))
