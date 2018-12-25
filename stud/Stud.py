import time


def repeat_three_times(func):
    def wrapper(*args, **kwargs):
        for _ in range(3):
            func(*args, **kwargs)

    return wrapper


def repeat(times):
    if not type(times) is int: raise Exception

    def real_decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)

        return wrapper

    return real_decorator


def with_info(func):
    def wrapper(*args, **kwargs):
        print(func.__name__, '\n', func.__module__)
        if args:
            print('arguments {}'.format(*args))
        if kwargs:
            print('arguments {}'.format(*kwargs))

        time1 = time.time()
        func(*args, **kwargs)
        print(time.time() - time1)

    return wrapper


@with_info
def return_max_of_three_last(seq):
    *rest, three, two, one = seq
    return max(one, two, three)


return_max_of_three_last([4, 545, 3, 234234])
