def cache(func):
    def wrapper(*args, **kwargs):
        if args[0] in wrapper.log:
            return wrapper.log[args[0]]
        else:
            result = func(*args, **kwargs)
            wrapper.log[args[0]] = result
            return result
    wrapper.log = {}
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)
fibonacci(4)
print(fibonacci.log)
