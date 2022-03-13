import turtle           # 터틀 모듈 불러오기
t = turtle.Turtle()     # 터틀 객체 t의 생성
t.shape("turtle")       # t의 모양을 거북이로 변경

# 각 원의 좌표와 반지름 입력 후 정수로 변환
x1 = int(input("큰 원의 중심좌표 x1: "))
y1 = int(input("큰 원의 중심좌표 y1: "))
r1 = int(input("큰 원의 반지름: "))
x2 = int(input("작은 원의 중심좌표 x2: "))
y2 = int(input("작은 원의 중심좌표 y2: "))
r2 = int(input("작은 원의 반지름: "))

t.penup()               # t를 들어올림(그리기 비활성화)
t.goto(x1,y1-r1)        # t를 (x1, y1-r1)으로 이동
t.pendown()             # t를 들어올림(그리기 활성화)
t.circle(r1)            # t로 반지름이 r1인 원 그리기

t.penup()               # t를 들어올림(그리기 비활성화)
t.goto(x2,y2-r2)        # t를 (x2, y2-r2)으로 이동
t.pendown()             # t를 들어올림(그리기 활성화)
t.circle(r2)            # t로 반지름이 r2인 원 그리기

# (x1, y1)와 (x2, y2) 사이의 거리 구하기
d = ( (x2-x1)**2 + (y2-y1)**2 )**0.5

# if와 elif를 이용하여 두 원의 관계를 판단하여 t로부터 내용 출력
if d > r1 - r2 and d < r1 + r2 :
    t.write("두 개의 원이 두 점에서 만나고 있습니다.")
elif r1 + r2 == d : 
    t.write("두 개의 원이 서로 외접하고 있습니다.")
elif r1 - r2 == d : 
    t.write("두 개의 원이 서로 내접하고 있습니다.")
elif r1 + r2 < d : 
    t.write("두번째 원이 첫번째 원의 외부에 있습니다.")
elif r1 - r2 > d : 
    t.write("두번째 원이 첫번째 원의 내부에 있습니다.")
