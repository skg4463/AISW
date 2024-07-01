# 학생 성적 데이터를 입력받는 함수
def input_student_data():
    students = {}  # 학생 데이터를 저장할 딕셔너리 초기화
    while True:
        name = input("학생 이름을 입력하세요 (종료하려면 '끝' 입력): ")
        if name == '끝':  # '끝'을 입력하면 반복 종료
            break
        subjects = {}  # 과목 성적을 저장할 딕셔너리 초기화
        while True:
            subject = input("과목 이름을 입력하세요 (종료하려면 '끝' 입력): ")
            if subject == '끝':  # '끝'을 입력하면 과목 입력 반복 종료
                break
            score = int(input(f"{subject} 성적을 입력하세요: "))  # 성적 입력받아 정수로 변환
            subjects[subject] = score  # 과목과 성적을 딕셔너리에 저장
        students[name] = subjects  # 학생 이름을 키로, 과목 성적 딕셔너리를 값으로 저장
    return students  # 학생 데이터 반환

# 학생 성적을 계산하는 함수
def calculate_results(students):
    results = {}  # 계산 결과를 저장할 딕셔너리 초기화
    for name, subjects in students.items():  # 각 학생의 데이터를 반복
        total = sum(subjects.values())  # 과목 성적의 총점 계산
        average = total / len(subjects)  # 과목 성적의 평균 계산
        results[name] = {
            'total': total,
            'average': average,
            'pass': '합격' if average >= 70 else '불합격'  # 평균이 70 이상이면 합격, 아니면 불합격
        }
    return results  # 계산 결과 반환

# 계산 결과를 출력하는 함수
def print_results(results):
    for name, data in results.items():  # 각 학생의 결과 데이터를 반복
        print(f"\n{name}의 총점: {data['total']}, 평균: {data['average']:.2f}")  # 총점과 평균 출력
        print(f"{name}는 {data['pass']}입니다.")  # 합격 여부 출력

    # 평균 성적이 가장 높은 학생 찾기
    highest_score_student = max(results, key=lambda x: results[x]['average'])
    # 평균 성적이 가장 낮은 학생 찾기
    lowest_score_student = min(results, key=lambda x: results[x]['average'])

    # 가장 높은 성적과 가장 낮은 성적 학생 출력
    print(f"\n성적이 가장 높은 학생: {highest_score_student} ({results[highest_score_student]['average']:.2f}점)")
    print(f"성적이 가장 낮은 학생: {lowest_score_student} ({results[lowest_score_student]['average']:.2f}점)")

# 메인 함수
def main():
    students = input_student_data()  # 학생 데이터를 입력받음
    results = calculate_results(students)  # 성적을 계산함
    print_results(results)  # 결과를 출력함

# 프로그램의 진입점
if __name__ == "__main__":
    main()  # 메인 함수 실행
