# 스타크래프트 프로젝트
# 출처: 나도코딩(https://youtu.be/kWiCuklohdY?t=13088)

from random import *

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print(f"{self.name} 유닛이 생성되었습니다.")

    def move(self, location):
        print(f"{self.name} : {location} 방향으로 이동합니다. [속도: {self.speed}]")

    def damaged(self, damage):
        print(f"{self.name} : {damage} 데미지를 입었습니다.")
        self.hp -= damage
        print(f"{self.name} : 현재 체력은 {self.hp} 입니다.")
        if self.hp <= 0:
            print(f"{self.name} : 파괴되었습니다.")


# 공격 유닛(Unit 상속받음)
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        # Unit.__init__(self, name, hp, speed)
        super().__init__(name, hp, speed)   # super()에서는 self 생략
        self.damage = damage

    def attack(self, location):
        print(f"{self.name} : {location} 방향으로 적군을 공격합니다. [공격력 {self.damage}]")


# 공중에 떠 있을 수 있음을 나타내는 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(f"{name} : {location} 방향으로 날아갑니다. [속도: {self.flying_speed}]")


# 공중 공격 유닛(AttackUnit 및 Flyable 다중 상속받음)
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):   # move() 메소드 오버라이딩
        self.fly(self.name, location)