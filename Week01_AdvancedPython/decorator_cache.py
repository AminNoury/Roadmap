# Placeholder for decorator_cache.py
def decorator(func):
    def wraper():
        print("start function")
        func()
        print("ending function")
    return wraper


@decorator
def test():
    print("midel")

test()
