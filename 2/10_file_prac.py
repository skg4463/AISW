import csv

# 학생 성적을 CSV 파일에 쓰는 함수
def write_grades(filename, students):
    # 'filename' 파일을 쓰기 모드로 열기
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)  # CSV 작성기 생성
        writer.writerow(["Name", "Math", "Science", "English"])  # 헤더 작성
        for student in students:  # 각 학생의 성적을 반복
            writer.writerow(student)  # 학생 성적을 파일에 작성

# CSV 파일에서 학생들의 평균 성적을 계산하는 함수
def calculate_averages(filename):
    # 'filename' 파일을 읽기 모드로 열기
    with open(filename, 'r') as file:
        reader = csv.reader(file)  # CSV 읽기 객체 생성
        next(reader)  # 헤더 건너뛰기
        averages = []  # 평균 성적을 저장할 리스트 초기화
        for row in reader:  # 각 학생의 성적을 반복
            name = row[0]  # 첫 번째 열은 학생 이름
            grades = list(map(int, row[1:]))  # # 첫 번째 요소를 제외한 나머지 성적을 정수 리스트로 변환
            average = sum(grades) / len(grades)  # 성적의 평균 계산
            averages.append((name, average))  # (이름, 평균 성적) 형태로 리스트에 추가
        return averages  # 평균 성적 리스트 반환

# 학생 성적 데이터
students = [
    ["Alice", 85, 90, 88],  # Alice의 성적
    ["Bob", 75, 80, 70]  # Bob의 성적
]

# 학생 성적을 'students.csv' 파일에 쓰기
write_grades('files/10_students.csv', students)

# 'students.csv' 파일에서 학생들의 평균 성적 계산
averages = calculate_averages('files/10_students.csv')

# 각 학생의 평균 성적 출력
for name, average in averages:
    print(f"{name}의 평균 성적: {average:.2f}")  # 소수점 둘째 자리까지 출력
