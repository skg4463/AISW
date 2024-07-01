def print_results(averages):
    highest_score_student = max(averages, key=averages.get)  # 최고 성적 학생
    lowest_score_student = min(averages, key=averages.get)  # 최저 성적 학생

    for name, average in averages.items():  # 각 학생에 대해
        status = "합격" if average >= 70 else "불합격"  # 합격/불합격 판단
        print(f"{name}의 평균 성적: {average:.2f} ({status})")  # 결과 출력

    print(f"\n성적이 가장 높은 학생: {highest_score_student} ({averages[highest_score_student]:.2f})")  # 최고 성적 학생 출력
    print(f"성적이 가장 낮은 학생: {lowest_score_student} ({averages[lowest_score_student]:.2f})")  # 최저 성적 학생 출력
