# 부모 클래스
class Unit:
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp
        print("{} 유닛이 생성되었습니다.".format(self.name))
    def move(self):
        print("[지상 유닛 이동]")


class Flyable:
    def __init__(self,flying_speed):
        self.flying_speed = flying_speed
    def fly(self,name, location):
        print("{} : {} 방향으로 날아갑니다. [속도 : {}]".format(name,location,self.flying_speed))

# 단일 상속
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        # super().__init__(name,hp)
        Unit.__init__(self,name, hp) # 이것도 됨 근데 다중상속 때문에 이게 나을듯
        self.damage = damage
        print("체력 {}, 공격력 {}".format(self.hp,self.damage))
    def attack(self,location):
        print("{} : {} 방향으로 적군을 공격합니다. [공격력 {}]".format(self.name,location,self.damage))
    def damaged(self, damage):
        self.hp -= damage
        print("{} 현재 체력은 {}입니다.".format(self.name,self.hp))
        if self.hp <= 0:
            print("{} 파괴되었습니다.".format(self.name))

firebat1 = AttackUnit('파이어뱃', 50, 16)
firebat1.attack("3시")
firebat1.damaged(26)
firebat1.damaged(26)

# 다중 상속, 메소드 오버라이딩
class FlyableAttackUnit(AttackUnit,Flyable):
    def __init__(self,name,hp,damage,flying_speed):
        AttackUnit.__init__(self,name,hp,damage)
        Flyable.__init__(self,flying_speed)
    def move(self,location): # 부모 크래스인 Unit에 이미 move가 정해져 있는데 그냥 하위에서 이렇게 한번 더 정의하면 다르게 쓸 수 있음
        print("[공중 유닛 이동]")    
        self.fly(self.name,location) # 이렇게 하면 내가 지금 쓰려는 move에 fly를 그냥 포함시켜서 한번에 처리 가능하다 

valkyrie = FlyableAttackUnit('발키리', 200, 6, 5)
valkyrie.move("3시")
valkyrie.attack("3시")
valkyrie.damaged(61)
valkyrie.damaged(61)
valkyrie.damaged(61)
valkyrie.damaged(61)

# pass 일단 다른작업 하다가 오고 싶을때 일단 pass 적어놓는거
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass

supply_depot = BuildingUnit('서플라이 디폿', 500, '7시')

def game_start():
    print('[알림] 게임을 시작합니다.')

def game_over():
    pass

game_start()
game_over()

