# decorator explain
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.\n")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()


# multi decorator
def decorator1(func):
    def wrapper():
        print("Decorator 1")
        func()
        print("End of Decorator 1")
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2")
        func()
        print("End of Decorator 2")
    return wrapper

@decorator1
@decorator2
def say_hello():
    print("Hello!")

say_hello()


# decorator with parameter
"""
데코레이터를 사용하여 사이의 함수에 인자를 전달
이 예제에서 greet 함수는 두 개의 인자를 받는다: name과 message
데코레이터 my_decorator는 이 인자들을 받아서 원래 함수인 greet에 전달
wrapper 함수는 가변 인자 *args와 **kwargs를 받아, 이를 통해 어떤 인자도 받을 수 있음

func(*args, **kwargs) 구문은 원래 함수를 호출하면서, 전달된 인자들을 그대로 전달
이 구문 덕분에 데코레이터는 원래 함수의 인자에 대해 신경 쓰지 않고, 다양한 인자를 처리할 수 있음

*args와 **kwargs를 사용하면 데코레이터가 다양한 인자를 유연하게 처리
"""
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.\n")
        return result
    return wrapper

@my_decorator
def greet(name, message):
    print(f"{message}, {name}!")

greet("Alice", "Hello")