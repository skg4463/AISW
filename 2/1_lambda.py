add_three = lambda x, y, z: x + y + z
print(add_three(1, 2, 3))  # 6

words = ["apple", "banana", "cherry", "date"]
long_words = list(filter(lambda word: len(word) >= 5, words))
print(long_words)  # ['apple', 'banana', 'cherry']

