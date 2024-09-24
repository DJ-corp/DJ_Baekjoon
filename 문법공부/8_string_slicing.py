# 슬라이싱
jumin = "951234-1234567"
print("생일 : {}".format(jumin[2:6])) # index 2번부터 5번까지
print("성별 : {}".format(jumin[7:8])) # index 7번만
print("성별 : {}".format(jumin[7])) # index 7번만
print("주민번호 뒷자리 : {}".format(jumin[7: ])) # index 7번부터 끝까지
print("주민번호 뒷자리 : {}".format(jumin[-7: ])) # index 뒤에서부터 하면 끝은 -1
print("주민번호 앞자리 : {}".format(jumin[ : 6])) # index 0부터 5까지
