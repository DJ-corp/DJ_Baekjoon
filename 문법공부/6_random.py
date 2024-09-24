# 랜덤 함수
from random import *

for i in range(0,100):
    print(random()) # 0 <= x < 1 인 실수
    print(random() * 10) # 0 <= x < 10 인 실수
    print(random() * 27 + 1) # 1 <= x < 28 인 실수
    print(randrange(0, 10)) # 0 <= x < 10 인 정수
    print(randrange(10)) # 0 <= x < 10 인 정수, 앞 글자를 안적으면 자동으로 0부터
    print(randint(0, 3)) # 0 <= x <= 10 인 정수, 아ㅍ 글자를 안적으면 오류남