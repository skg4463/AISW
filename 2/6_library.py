import math
print(math.pi)  # 3.141592653589793
print(math.e)   # 2.718281828459045
print(math.sqrt(16))  # 4.0

import datetime
now = datetime.datetime.now()
print(now)  # 현재 날짜와 시간 출력

import os
print(os.name)  # 운영체제 이름 출력
print(os.getcwd())  # 현재 작업 디렉토리 출력

import sys
print(sys.version)  # 파이썬 버전 정보 출력

import os
files = os.listdir('..')
print(files)  # 현재 디렉토리의 파일 목록 출력

import datetime
now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # 2024-07-02 14:30:00
