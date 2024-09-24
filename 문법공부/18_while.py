# while 문

index = 5

while index >= 1:
    guest = input("지금 어떤 손님 차례인가요? ")
    target = "송재준"
    if guest == target:
        print("{}님 음료 준비되었습니다.".format(guest))
        index = 0
    elif index == 1:
        print("{}님 안계시기 때문에 음료 폐기하겠습니다.".format(target))
        index -= 1    
    else:
        print("{}님 안계신가요?".format(target))
        index -= 1    