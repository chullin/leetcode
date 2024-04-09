import time

def timing(func):
    def wrapper():
        print("Start...")
        t1 = time.perf_counter()
        func()
        t2 = time.perf_counter()
        print("Elapsed time(secs):", t2 - t1)
    return wrapper


def check_str(func):
    def inner_func():
        print('This is inner function')
        return func()
    return inner_func


@timing
@check_str
def hello():
    print('Hello World')

# 順序交換，效果會不同
@check_str
@timing
def world():
    print('World Hello ')

hello()
world()