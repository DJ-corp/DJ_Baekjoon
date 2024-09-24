# if
a = int(input("숫자를 입력해주세요 : ")) # input은 출력이 str로 되기 때문에 int로 감싸서 비교해줘야 한다.
if a == 1:
    print(str(a) + "는 1이다.")
elif a == 2:
    print(str(a) + "는 2이다.")
else:
    print(str(a) + "이 뭔지 모르겠다.")

# for문까지 해봤다.

for i in range(0,10):
    b = int(input("숫자를 넣어보자 : " ))
    if b >= 40:
        print("온도가 40도 이상입니다.")
    elif b < 40 and b >= 20:
        print("온도가 20이상 40미만이다.")
    else:
        print("온도가 20 미만이다.")    