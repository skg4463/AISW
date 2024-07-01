import csv


def calculate_averages(filename):
    with open(filename, 'r') as file:  # CSV 파일을 읽기 모드로 열기
        reader = csv.reader(file)  # CSV 읽기 객체 생성
        next(reader)  # 헤더 건너뛰기
        student_scores = {}  # 학생 성적을 저장할 딕셔너리
        for row in reader:
            name, subject, score = row  # 각 행에서 이름, 과목, 성적 추출
            score = int(score)  # 성적을 정수로 변환
            if name not in student_scores:  # 학생 이름이 딕셔너리에 없으면
                student_scores[name] = []  # 새로운 리스트 생성
            student_scores[name].append(score)  # 성적 리스트에 추가

        averages = {}  # 학생별 평균 성적을 저장할 딕셔너리
        for name, scores in student_scores.items():
            average = sum(scores) / len(scores)  # 평균 성적 계산
            averages[name] = average  # 딕셔너리에 저장

        return averages  # 평균 성적 딕셔너리 반환
