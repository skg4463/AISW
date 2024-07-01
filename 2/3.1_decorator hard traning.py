import time

'''
함수의 실행 시간을 측정하는 데코레이터를 작성
함수 호출 횟수를 세는 데코레이터를 작성
'''
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time} seconds to complete")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(2)
    print("Function is done")

slow_function()

def call_counter(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"Call {wrapper.calls} of function {func.__name__}")
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

@call_counter
def say_hello():
    print("Hello!")

say_hello()
say_hello()
