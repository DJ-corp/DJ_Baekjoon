''' 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

	(출력 예제)
	총 3대의 매물이 있습니다.
	강남 아파트 매매 10억 2010년
	마포 오피스텔 전세 5억 2007년
	송파 빌라 월세 500/50 2000년
	
	class House:
	    # 매물 초기화 : 위치, 건물 종류, 매물 종류, 가격, 준공년도
	    def __init__(self, location, house_type, deal_type, price, completion_year):
	        pass
	    
	    # 매물 정보 표시
	    def show_detail(self):
	        pass'''

class House:
    def __init__(self, location, house_type, deal_type,price,completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print("{} {} {} {} {}년".format(self.location,self.house_type,self.deal_type,self.price,self.completion_year))
houses = []
a = House("강남","아파트","매매","10억",2010)
b = House("마포","오피스텔","전세","5억",2007)
c = House("송파","빌라","월세","500/50",2000)
houses.append(a)
houses.append(b)
houses.append(c)
print("총 {}개의 매물이 있습니다.".format(len(houses)))
for house in houses:
    house.show_detail()
# (출력 예제)
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년