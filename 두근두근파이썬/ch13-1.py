from math import pi

# 클래스 생성
class Circle():

    # 생성자
    def __init__(self, radius):
        self.radius = float(radius)

    # 원 둘레 계산 함수
    def calcPerimeter(self):
        return self.radius * 2 * pi

    # 원 면적 계산 함수
    def calcArea(self):
        return self.radius**2 * pi

r = input("반지름: ")

# 객체 생성
c = Circle(r)

print("원의 면적:", c.calcPerimeter())
print("원의 둘레:", c.calcArea())
