import time
cache = {}


def exps(x, y, z):
    # Implement me

    # use a tuple as the Key
    if (x, y, z) in cache.keys():
        return cache[(x, y, z)]

    result = None
    if x <= 0:
        result = y + z
    if x > 0:
        result = exps(x-1, y+1, z) + exps(x-2, y+2, z*2) + exps(x-3, y+3, z*3)

    # use a tuple as the Key
    cache[(x, y, z)] = result
    return result


if __name__ == "__main__":
    start = time.time()

    for i in range(100):
        x = exps(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(exps(150, 400, 800))
    print("Imp 1: \t%.8f" % float(time.time() - start))
