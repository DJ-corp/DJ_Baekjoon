# continue, break  
absent = [2,5]
no_book = [7]

for reader in range(1,21):
    if reader in absent:
        print("{}번은 오늘 결석이구나".format(reader))
        continue
    elif reader in no_book:
        print("{}번 너는 안되겠다 교무실로 따라와".format(reader))
        break
    print("{}번 책을 읽어봐".format(reader))
    