# 스타크래프트 프로젝트
# 출처: 나도코딩(https://youtu.be/kWiCuklohdY?t=13088)

from unit_types import *
from random import *

# 마린(AttackUnit 상속받음)
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    # 스팀팩: 일정 시간 동안 이동 및 공격 속도를 증가, 자기 체력 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print(f"{self.name} : 스팀팩을 사용합니다. (HP 10 감소)")
        else:
            print(f"{self.name} : 체력이 부족하여 스팀팩을 사용하지 않습니다.")

# 탱크(AttackUnit 상속받음)
class Tank(AttackUnit):
    # 시즈모드: 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능. 이동 불가
    seize_developed = False

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.sezie_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return

        # 현재 시즈모드가 아닐 때 -> 시즈모드
        if self.sezie_mode == False:
            print(f"{self.name} : 시즈모드로 전환합니다.")
            self.damage *= 2
            self.seize_mode = True

        # 현재 시즈모드일때 -> 시즈모드 해제
        else:
            print(f"{self.name} : 시즈모드를 해제합니다.")
            self.damage /= 2
            self.seize_mode = False

# 레이스(FlyableAttackUnit 상속받음)
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False

    def clocking(self):
        # 현재 클로킹 모드가 아닐 때 -> 클로킹 모드
        if self.clocked == True:
            print(f"{self.name} : 클로킹 모드를 해제합니다.")
            self.clocked = False

        # 현재 클로킹 모드일때 -> 클로킹 모드 해제
        else:
            print(f"{self.name} : 클로킹 모드를 설정합니다.")
            self.clocked = True