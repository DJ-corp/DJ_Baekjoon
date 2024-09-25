# sep, end
print("송재준","양다은",sep = "zz")
print("송재준","양다은",sep = "")
print("송재준","양다은",sep = "&")
print("송재준","양다은")

print("송재준","양다은",sep = "&",end = " ")
print("송재준","양다은",end = "&")
print("송재준","양다은",end = "*")
print("송재준","양다은",end = "%")

# 표준 출력(stdout), 표준 에러(stderr) / 지긍믕 의미가 없다.
import sys

print("Python", "Java", file=sys.stdout) # Python Java
print("Python", "Java", file=sys.stderr) # Python Java

# ljust, rjust
scores = {"수학" : 30, "영어" : 10, "과학" : 5}
for subject, scroe in scores.items():
    print(subject.ljust(4),str(scroe).rjust(10),sep = ":")

# zfill
for number in range(1,21):
    print("대기번호 : {}번 손님 주문하신 음료 나왔습니다.".format(str(number).zfill(3)))