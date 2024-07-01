# map function
nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, nums))
print('squared: ', squared)  # [1, 4, 9, 16, 25]

# filter function
even = list(filter(lambda x: x % 2 == 0, nums))
print('even: ', even)  # [2, 4]

# reduce function
from functools import reduce

product = reduce(lambda x, y: x * y, nums)
print('protocol: ', product, '\n')  # 120

# example
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum_all = reduce(lambda x, y: x + y, nums)
print(sum_all)  # 55

even_squared = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums)))
print(even_squared)  # [4, 16, 36, 64, 100]
