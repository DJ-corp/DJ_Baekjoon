''' 변수를 이용하여 다음 문장을 출력하시오.
		
    변수명
    : station
    
    변수값
    : “사당”, “신도림”, “인천공항”
    
    출력문장
    : xx행 열차가 들어오고 있습니다.'''

stations = ["사당", "신도림", "인천공항"]

for station in stations:
    print("{}행 열차가 들어오고 있습니다.".format(station))