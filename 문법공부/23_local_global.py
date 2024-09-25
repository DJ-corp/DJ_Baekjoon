# # 지역변수를 선언하지 않고 전역변수만 믿고 깝친 경우
# gun= 10

# def checkpoint(soldiers):
#     gun = gun - soldiers
#     print("지금 남아있는 총 개수 : {}".format(gun))

# print("전체 총 : {}".format(gun))
# checkpoint(2)
# print("남은 총 : {}".format(gun))

# # 지역변수를 선언한다면?
# gun= 10

# def checkpoint(soldiers):
#     gun = 10 # 이 지역변수 gun은 저 전역변수 gun이랑은 관계가 없음 return을 해서 전역변수gun에 저장을 해야 의미가 있는것
#     gun = gun - soldiers
#     print("지금 남아있는 총 개수 : {}".format(gun))

# print("전체 총 : {}".format(gun))
# checkpoint(2)
# print("남은 총 : {}".format(gun))

# 지역변수를 선언한다면?
gun= 10

def checkpoint(soldiers):
    global gun # 이렇게 전역변수로 애초에 받아오면 그 전역변수 자체를 조작할 수 있음
    gun = gun - soldiers
    print("지금 남아있는 총 개수 : {}".format(gun))

print("전체 총 : {}".format(gun))
checkpoint(2)
print("남은 총 : {}".format(gun))

# 그냥 정석
gun= 10

def checkpoint(gun, soldiers):
    gun = gun - soldiers
    print("지금 남아있는 총 개수 : {}".format(gun))
    return gun

print("전체 총 : {}".format(gun))
gun = checkpoint(gun, 2)
print("남은 총 : {}".format(gun))