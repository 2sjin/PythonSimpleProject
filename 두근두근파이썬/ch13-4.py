import turtle

# Turtle 클래스를 상속받은 서브클래스 MyTurtle
class MyTurtle(turtle.Turtle):

    # 사각형 그리기 함수
    def drawSquare(self):
        for i in range(4):
            self.right(90)
            self.forward(100)

# 객체 생성 및 함수 호출]
my_turtle = MyTurtle()
my_turtle.forward(100)
my_turtle.drawSquare()
