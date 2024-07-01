import csv

# CSV 파일을 딕셔너리 형태로 쓰기
def write_csv_as_dict(file_path, data):
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['Name', 'Age', 'City'] # 열 제목을 정의
        writer = csv.DictWriter(file, fieldnames=fieldnames)  # DictWriter 객체 생성
        writer.writeheader()  # 열 제목을 파일에 작성
        writer.writerows(data) # 데이터 작성

# CSV 파일을 딕셔너리 형태로 읽기
def read_csv_as_dict(file_path):
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)

# 사용 예제
data = [
    {'Name': 'Alice', 'Age': 30, 'City': 'New York'},
    {'Name': 'Bob', 'Age': 25, 'City': 'San Francisco'},
    {'Name': 'Charlie', 'Age': 35, 'City': 'Los Angeles'}
]
write_csv_as_dict('files/9.1_example.csv', data)
read_csv_as_dict('files/9.1_example.csv')

