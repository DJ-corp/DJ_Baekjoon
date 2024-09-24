# 사전 생성 및 단순 출력
cabinet = {4 : "유재석", 100 : "김태호"}
print(cabinet)
print(cabinet[4])
print(cabinet.get(4))
print(cabinet.get(5)) # NONE 반환 cabinet[5]로 하면 그냥 오류 뜸
print(cabinet.get(5,"없음")) # NONE 반환 시 "없음"으로 뜨게 함
print(5 in cabinet) # 그 값이 cabinet에 있냐?
cabinet[4] = "송재준"
print(cabinet[4])
print(cabinet)
del cabinet[4]
print(cabinet)
cabinet[23] = "김종국"
print(cabinet)
cabinet_dict_list = cabinet.keys()
print(cabinet_dict_list) # dict_keys[list] 이런식으로 나와서 리스트로 만들라면 아래와 같이 써야함
cabinet_list = list(cabinet.keys())
print(cabinet_list)
cabinet_value_list = list(cabinet.values())
print(cabinet_value_list)
cabinet_item_list = list(cabinet.items()) # 튜플 자체를 리스트로 반환
print(cabinet_item_list)
cabinet.clear()
print(cabinet)