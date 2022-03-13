import turtle           # 터틀 모듈 불러오기
t = turtle.Turtle()     # 터틀 객체 t의 생성
t.shape("turtle")       # t의 모양을 거북이로 변경

# 색상1, 색상2, 색상3 입력
color1 = input("색상 #1을 입력하시오: ")
color2 = input("색상 #2을 입력하시오: ")
color3 = input("색상 #3을 입력하시오: ")

r = 50                  # 반지름 50으로 초기화

t.fillcolor(color1)     # 채우기 색을 color1로 설정
t.begin_fill()          # 채우기 시작
t.circle(r)             # 반지름 r인 원 그리기
t.end_fill()            # 채우기 종료

t.penup()               # t를 들어올림(그리기 비활성화)
t.forward(r * 2)        # r * 2 만큼 앞으로 이동
t.pendown()             # t를 들어올림(그리기 활성화

t.fillcolor(color2)     # 채우기 색을 color2로 설정
t.begin_fill()          # 채우기 시작
t.circle(r)             # 반지름 r인 원 그리기
t.end_fill()            # 채우기 종료

t.penup()               # t를 들어올림(그리기 비활성화)
t.forward(r * 2)        # r * 2 만큼 앞으로 이동
t.pendown()             # t를 들어올림(그리기 활성화

t.fillcolor(color3)     # 채우기 색을 color3로 설정
t.begin_fill()          # 채우기 시작
t.circle(r)             # 반지름 r인 원 그리기
t.end_fill()            # 채우기 종료
