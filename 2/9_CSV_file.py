import csv

# CSV 파일 쓰기
with open('files/9_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Math", "Science", "English"])
    writer.writerow(["Alice", 85, 90, 88])
    writer.writerow(["Bob", 75, 80, 70])

# CSV 파일 읽기
with open('files/9_data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
