# python_any2

a = open("python_any2.txt", "w")
a.write("Typing Any")
a.close()

# --------------------------------------

import random

d = str(random.randint(1,77919826982982) / random.randrange(1, 76))

t = open("python_any2_2.txt", "w")
t.write("The Password is " + d + ".")
t.close()

i = 0

while True:
    i = input("숫자를 입력하세요: ")
    if i == d:
        print("파일을 확인하셨군요.")
        break
    else:
        print("잘못 입력하셨습니다. 혹시 파일이 생겼다던지 그렇진 않은가요?")

# ----------------------------------------

import os

os.remove("python_any2.txt")
os.remove("python_any2_2.txt")