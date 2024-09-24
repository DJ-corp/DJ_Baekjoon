# 변수 선언
pet = "강아지"
name = "송재준"
age = 4
hobby = "산책"
is_adult = age > 3

# 정답지
print("우리집의 강아지는 이름이 송재준입니다.")
print("송재준의 나이는 4이며 산책을 가장 좋아합니다.")
print("근데 우리 강아지는 어른이 된건가요? True")

# +를 이용 : 숫자형과 boolean형에는 str로 감싸줘야함
print("우리집의 " + pet + "는 이름이 " + name +"입니다.")
print(name + "의 나이는 " + str(age) + "이며 " + hobby + "을 가장 좋아합니다.")
print("근데 우리 " + pet +"는 어른이 된건가요?" + str(is_adult))

# format을 이용 : str로 감싸지 않아도 출력 됨 감싸도 됨
print("우리집의 {}는 이름이 {}입니다.".format(pet,name))
print("{}의 나이는 {}이며 {}을 가장 좋아합니다.".format(name,age,hobby))
print("근데 우리 {}는 어른이 된건가요? {}".format(pet,is_adult))
print("근데 우리 {1}는 어른이 된건가요? {0}".format(pet,is_adult)) # 이렇게 아예 순서 지정해서 사용도 가능
