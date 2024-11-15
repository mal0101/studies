import time    


def cache(function):
    cache_data = {}
    call_count = 0

    def wrapper(*args):
        nonlocal call_count
        call_count += 1
        if args in cache_data:
            print(f"Using cached value for {args}")
            return cache_data[args]
        start_time = time.time()
        result = function(*args)
        end_time = time.time()
        cache_data[args] = result
        print(f"Execution time: {end_time - start_time} seconds")
        print(f"Number of calls: {call_count}")
        return result

    return wrapper

@cache
def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1)

    # Test the decorated function
# print(fact(3))
print(fact(5))