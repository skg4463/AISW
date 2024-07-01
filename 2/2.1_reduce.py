from functools import reduce

# 리스트의 모든 요소 산술연산------------------------
numbers = [1, 2, 3, 4, 5]

# reduce 함수를 사용하여 리스트의 모든 요소를 곱한다
product_of_numbers = reduce(lambda x, y: x * y, numbers)
print("리스트의 모든 요소 산술연산: ", product_of_numbers)  # 출력: 120

# 문자열 병합------------------------
words = ["Hello", "world", "this", "is", "Python"]

# reduce 함수를 사용하여 리스트의 모든 문자열을 연결한다
sentence = reduce(lambda x, y: x + " " + y, words)
print('문자열 병합: ', sentence)  # 출력: Hello world this is Python

# 리스트 병합------------------------
lists = [[1, 2, 3], [4, 5], [6, 7, 8]]

# reduce 함수를 사용하여 리스트를 합친다
flattened_list = reduce(lambda x, y: x + y, lists)
print('리스트 병합: ', flattened_list)  # 출력: [1, 2, 3, 4, 5, 6, 7, 8]

# 논리 연산------------------------
booleans = [True, True, False, True]

# reduce 함수를 사용하여 모든 요소가 참인지 확인한다
all_true = reduce(lambda x, y: x and y, booleans)
print('논리 연산: ', all_true)  # 출력: False

# 딕셔너리 병합------------------------
dicts = [{'a': 1}, {'b': 2}, {'c': 3}]

# reduce 함수를 사용하여 딕셔너리 병합
merged_dict = reduce(lambda x, y: {**x, **y}, dicts)
print('딕셔너리 병합: ', merged_dict)  # 출력: {'a': 1, 'b': 2, 'c': 3}

