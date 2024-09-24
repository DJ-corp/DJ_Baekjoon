# 문자열 처리함수
python = "Python is Amazing"
print(python.lower()) # 전부 소문자로 바꾸는 함수
print(python.upper()) # 전부 대문자로 바꾸는 함수
print(python[0].lower()) # 첫번째 글자만 소문자로 바꿔라
print(python[0].upper()) 
print(python[0].upper().islower()) # 첫번째 글자만 대문자로 바꾸고 소문자라면 true를 반환해라
print(python[0].lower().islower()) # 첫번째 글자만 소문자로 바꾸고 소문자라면 true를 반환해라
print(python[0].isupper())
print(len(python)) # 참고로 index는 공백도 포함임
print(python.replace("Python", "Java")) 
print("코드 종류 : {}".format(python[ : 6]))
index = python.index("i") # i의 인덱스를 반환해라, 찾는 값이 없으면 오류발생
print(index)
index = python.index("i", 8) # i의 인덱스를 인덱스 8부터 찾아봐라, 두번째 i의 인덱스를 반환함
print(index)
find = python.find("k") # k의 인덱스를 반환해라, 찾는 값이 없으면 -1출력
print(find)
