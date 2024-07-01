import csv

def input_student_data(filename):
    with open(filename, 'w', newline='') as file:  # CSV 파일을 쓰기 모드로 열기
        writer = csv.writer(file)  # CSV 작성자 객체 생성
        writer.writerow(["Name", "Subject", "Score"])  # 헤더 작성
        while True:
            name = input("학생 이름을 입력하세요 (종료하려면 '끝' 입력): ")  # 학생 이름 입력
            if name == '끝':  # '끝' 입력 시 루프 종료
                break
            while True:
                subject = input("과목 이름을 입력하세요 (종료하려면 '끝' 입력): ")  # 과목 이름 입력
                if subject == '끝':  # '끝' 입력 시 루프 종료
                    break
                score = int(input(f"{subject} 성적을 입력하세요: "))  # 성적 입력
                writer.writerow([name, subject, score])  # 입력받은 데이터를 CSV 파일에 작성
