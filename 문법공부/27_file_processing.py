# 파일을 읽고 써봅시다.
scores_file = open("scores.txt","w",encoding="utf-8")
scores_file.write("실습 : 400\n")
print("수학 : 0",file=scores_file)
print("영어 : 100",file=scores_file)
scores_file.close()

scores_file = open("scores.txt","a",encoding="utf-8")
print("과학 : 200",file=scores_file) # 그냥 이렇게 하는게 나을듯
scores_file.write("실습 : 400")
scores_file.write("\n기가 : 400")
scores_file.close()

scores_file = open("scores.txt","r",encoding="utf-8") # 전체를 읽는것
scores_file.read()
scores_file.close()

scores_file = open("scores.txt","r",encoding="utf-8") # 한줄씩 순서대로 읽는것
print(scores_file.readline(),end="")
print(scores_file.readline(),end="")
print(scores_file.readline(),end="")
print(scores_file.readline(),end="")
print(scores_file.readline(),end="")
scores_file.close()

scores_file = open("scores.txt","r",encoding="utf-8") # 한줄씩 순서대로 읽는것
for line in scores_file.readlines():
    print(line,end="")
scores_file.close()

scores_file = open("scores.txt","r",encoding="utf-8") # 한줄씩 순서대로 읽는것
while True:
    line = scores_file.readline()
    if not line == True:
        break
    print(line,end="")
scores_file.close()






