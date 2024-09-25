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



def withdraw(balance, money, time):
    if time > 18:
        commision = 100
    else:
        commision = 0
    if balance < money:
        print("잔고가 부족합니다. 부족한 잔고 {}".format(balance-money-commision))
        return balance
    else:
        print("{}원 인출이 완료되었습니다. 현재 잔고 {}원 입니다.".format(money, balance - money - commision))
    return balance - money - commision    

balance = withdraw(balance, 1000, 17)
print(balance)
balance = withdraw(balance, 1000, 19)
print(balance)
balance = withdraw(balance, 1000, 17)
print(balance)

# 기본값 사용

def student(name, age, lang):
    print("이름 : {}\t나이 : {}\t언어 : {}".format(name, age, lang))
student("송재준",15,"Python")    
student("양다은",13,"Java")

def student2(name, age = 15, lang = "Python"):
    print("이름 : {}\t나이 : {}\t언어 : {}".format(name, age, lang))
student2("송재준")    
student2("양다은",13,"Java")

def student3(name, lang, age): # 순서를 바꿔도 된다.
    print("이름 : {}\t나이 : {}\t언어 : {}".format(name, age, lang))
student("송재준",age = 15,lang = "Python")    
student("양다은",age = 13,lang = "Java")

def student4(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {}\t나이 : {}\t".format(name, age), end = "")
    print("언어 : "+lang1, lang2, lang3, lang4, lang5)
student4("송재준",15,"Python", "Java", "Kotlin", "C ++","Pypy")    
student4("양다은",13,"Java", "Js","","","") # 이렇게 ""으로 쓰면 안썯 된다.

def student4(name, age, *language): # 튜플로 받아오는것
    print("이름 : {}\t나이 : {}\t언어 : ".format(name, age), end = "")
    for lang in language:
        print(lang,end = " ")
    print()
student4("송재준",15,"Python", "Java", "Kotlin", "C ++","Pypy")    
student4("양다은",13,"Java", "Js") # 이렇게 ""으로 쓰면 안썯 된다.

def student5(name, age, *language): # 튜플로 받아오는것
    print("이름 : {}\t나이 : {}\t언어 : ".format(name, age), end = "")
    print(*language)
student5("송재준",15,"Python", "Java", "Kotlin", "C ++","Pypy")    
student5("양다은",13,"Java", "Js") # 이렇게 ""으로 쓰면 안써도 된다.