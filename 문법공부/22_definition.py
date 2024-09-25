# 함수
gun = 10 
def gunplus(gun):
    print("총이 한자루 추가되어 {}자루가 되었습니다.".format(gun+1))
    return gun + 1
gun = gunplus(gun)
print(gun)

def deposit(balance, money):
    print("고객님 {}원 입금이 확인되었습니다. 현재 잔액은 {}원 입니다. 감사합니다.".format(money, balance + money))
    return balance + money

balance = 0
balance = deposit(balance, 1000)
print(balance)
balance = deposit(balance, 2000)
print(balance)