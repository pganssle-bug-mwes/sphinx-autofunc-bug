__all__ = ['func']

def __get_func():
    class MyFunction:
        def __call__(self):
            print("Hello, world")
    return MyFunction()

func = __get_func()
del __get_func
