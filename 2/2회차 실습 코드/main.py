import student_input  # 학생 성적 입력 모듈
import student_calculate  # 성적 계산 모듈
import student_print  # 결과 출력 모듈

def main():
    filename = 'students.csv'  # CSV 파일 이름
    student_input.input_student_data(filename)  # 학생 성적 입력 함수 호출
    averages = student_calculate.calculate_averages(filename)  # 성적 계산 함수 호출
    student_print.print_results(averages)  # 결과 출력 함수 호출

if __name__ == "__main__":
    main()  # 메인 함수 호출
