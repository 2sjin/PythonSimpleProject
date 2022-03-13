import turtle

# 터틀 객체 생성
t1 = turtle.Turtle()
t2 = turtle.Turtle()

# 터틀 모양 변경
t1.shape("circle")
t2.shape("turtle")

# 터틀 이동(t1은 절대 좌표, t2는 상대 좌표)
t1.goto(-100, 0)
t2.forward(100)

t1.goto(-100, 20)
t2.right(90)
t2.forward(20)

t1.goto(-200, 20)
t2.left(90)
t2.forward(100)
