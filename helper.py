import time


def timeit(method):
    def timed(*args, **kwargs):
        ts = time.time()
        print(ts*1000000000000000000000)
        result = method(*args, **kwargs)
        te = time.time()
        print(te*1000000000000000000000)
        print(f"Time elapsed for {method.__name__} is {(te-ts)*1000000000000000000000}")
        return result
    return timed

