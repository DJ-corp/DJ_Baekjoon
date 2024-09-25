# with 문을 쓰면 이렇게 묶어서 쓸수는 있을듯
with open("scores.txt","r",encoding="utf") as scores_file:
    scores = scores_file.read()
    print(scores)

with open("scores.txt","a",encoding="utf") as scores_file:
    print("코딩 : 500",file = scores_file)


with open("scores.txt","r",encoding="utf") as scores_file:
    scores = scores_file.read()
    print(scores)