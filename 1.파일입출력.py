with open("test.txt","r",encoding="utf-8")as file:
	line1=file.readline()
	line2=file.readline()

print(line1)
print(line2)

with open("test.txt","r",encoding="utf-8")as file:
	lines=file.readlines()

print(lines)

for line in lines:
	print(line.strip())

with open("memo.txt","a",encoding="utf-8")as file:
	file.write("4일차 학습\n")

memo=input("메모를 입력하세요: ")

with open("memo.txt","w",encoding="utf-8")as file:
	file.write(memo)

while True:
	memo=input("메모를 입력하세요. 종료하려면 q 입력: ").strip()

	if memo.lower()=="q":
		break
	
	with open("memo.txt","a",encoding="utf-8")as file:
		file.write(memo+"\n")
	
	print("메모 저장이 완료되었습니다.")

students= [
{"name":"민수","score":85},
{"name":"지수","score":92},
{"name":"영희","score":55}
]

with open("students.txt","w",encoding="utf-8")as file:
	for student in students:
		file.write(f"{student['name']},{student['score']}\n")

def save_students(students, filename):
    with open(filename, "w", encoding="utf-8") as file:
        for student in students:
            line = f"{student['name']},{student['score']}\n"
            file.write(line)

save_students(students,"test.txt")

import os

if os.path.exists("ranking.txt"):
    print("랭킹 파일이 있습니다.")
else:
    print("랭킹 파일이 없습니다.")


def save_lotto(lotto):
    line = ""

    for i in range(len(lotto)):
        line += str(lotto[i])

        if i < len(lotto) - 1:
            line += ","

    with open("lotto_history.txt", "a", encoding="utf-8") as file:
        file.write(line + "\n")