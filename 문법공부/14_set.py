# 세트 (튜플은 생략) , 집합문서로 사용할수가 있다.
number = [1,2,3,3,3]
print(number)
number = set(number) # set로 바꿔주면 중복이 제거됨
print(number)
number.add(7)
print(number)


java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])
print(java & python) # 교집합
print(java | python) # 합집합
print(java - python) # 차집합

python.add("정준하")
print(python)
python.remove("정준하")
print(python)
