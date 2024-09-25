class Unit:
    def __init__(self,name,hp,damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {}, 공격력 {}".format(self.hp,self.damage))

marine1 = Unit("마린",40,5)
marine2 = Unit("마린",40,5)
tank = Unit("탱크",150,35)
wraith1 = Unit("레이스",80,5)
wraith2 = Unit("빼앗은레이스",80,5)
wraith2.cloacking = True
if wraith2.cloacking == True:
    print("{}는 현재 클로킹 상태입니다.".format(wraith2.name))

class AttackUnit:
    def __init__(self,name,hp,damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {}, 공격력 {}".format(self.hp,self.damage))
    def attack(self,location):
        print("{} : {} 방향으로 적군을 공격합니다. [공격력 {}]".format(self.name,location,self.damage))
    def damaged(self, damage):
        self.hp -= damage
        print("{} 현재 체력은 {}입니다.".format(self.name,self.hp))
        if self.hp <= 0:
            print("{} 파괴되었습니다.".format(self.name))

firebat1 = AttackUnit('파이어뱃', 50, 16)
AttackUnit.attack(firebat1,"3시")
AttackUnit.damaged(firebat1,35)
AttackUnit.damaged(firebat1,35)

