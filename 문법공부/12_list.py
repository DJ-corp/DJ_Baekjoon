# 문자열 자료형 리스트
subway = ["유재석", "조세호", "박명수"]
print(subway[0:3])
print(subway.index("조세호"))
subway.append("강호동")
subway.insert(2,"정형돈")
print(subway)
subway.pop()
print(subway.count("유재석"))
print(subway)
subway.sort()
print(subway)
subway.reverse()
print(subway)
subway.clear()
print(subway)

# 숫자열 자료형 리스트
number = [5,2,3,1,4]
number.sort() # 숫자일때 오름차순, 문자열일때도 오름차순 됨
print(number) 
number.reverse() # 숫자일때 내림차순, 문자열일때도 내림차순 됨
print(number)
number.pop()
print(number)
number.insert(4,100)
print(number)
number.clear()
print(number)

# 여러 리스트의 결합

subway = ["송재준", "유재석", "조세호"]
number = [1,2,3]
number.extend(subway)
print(number)

# 리스트로 입력하는법
number = list(map(int, input().split())) # 10 20 30 이렇게 입력하면 되고 int를 str로 바꾸면 문자열 자료형으로 나옴
print(number)