from multiprocessing.sharedctypes import Value
from tkinter import *
import time
import random

# 공(Ball) 클래스 정의
class Ball:
    # 생성자
    def __init__(self, canvas, color="blue", size=100, x=10, y=150, xspeed=0, yspeed=0):
        self.canvas = canvas
        self.color = color
        self.size = size
        self.x = x
        self.y = y
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.id = canvas.create_oval(x, y, x+size, y+size, fill=color)  # 캔버스 객체를 변수에 저장

    # 객체 정보 출력(매직 메소드)
    def __str__(self):
        msg = f"색상({self.color})\t크기({self.size})\t좌표({self.x}, {self.y})\t속도({self.xspeed}, {self.yspeed})"
        return msg

    # 공을 이동시키는 함수(메소드)
    def move(self):
        self.canvas.move(self.id, self.xspeed, self.yspeed)

        (x1, y1, x2, y2) = self.canvas.coords(self.id)  # 공의 좌상단 좌표(x1, y1)와 우하단(x2, y2) 좌표 얻기
        (self.x, self.y) = (x1, y1)

        # 공이 화면을 벗어나면 방향 전환
        if x1 <= 0 or x2 >= WIDTH:
            self.xspeed = -self.xspeed
        if y1 <= 0 or y2 >= HEIGHT:
            self.yspeed = -self.yspeed

        # 포탄과 충돌 시 객체 삭제
        for bullet in bullets_list:
            if x1 <= bullet.x <= x2 and y1 <= bullet.y <= y2:
                canvas.delete(self.id)    # 캔버스에서 공 삭제
                try:
                    balls_list.remove(self)   # 리스트에서 공 삭제
                except Value:
                    pass    # 이미 삭제된 객체를 요구할 경우 무시

# 포탄(Bullet) 클래스 정의(부모 클래스 Ball로부터 상속)
class Bullet(Ball):
    def __init__(self):
        super().__init__(canvas, "red", 10, 110, 200, 15, 0)

    # 포탄을 이동시키는 함수(메소드)
    def move(self):
        self.canvas.move(self.id, self.xspeed, self.yspeed)
        self.x += self.xspeed
        
        # 포탄이 화면을 벗어나면 객체 삭제
        if (self.x + self.size) >= WIDTH:
            canvas.delete(self.id)      # 캔버스에서 포탄 삭제
            try:
                bullets_list.remove(self)   # 리스트에서 포탄 삭제
            except Value:
                pass    # 이미 삭제된 객체를 요구할 경우 무시


# 포탄 발사(마우스 좌클릭 시)
def fire(event):
    new_bullets = Bullet()  # 포탄(Bullet 객체) 생성
    bullets_list.append(new_bullets)    # 포탄 발사

# 변수 초기화
color_list = ["yellow", "green", "orange", "pink"]
balls_list = []     # 공들이 저장되는 리스트
bullets_list = []    #
WIDTH, HEIGHT = 800, 400    # 윈도우의 가로 세로 크기(상수처럼 사용)

# GUI 환경 구성(윈도우, 캔버스)
window = Tk()
canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()
canvas.bind("<Button-1>", fire)     # 마우스 좌클릭 시 함수 호출

# 랜덤 값 저장 및 공(Ball 객체) 생성
for i in range(10):
    color = random.choice(color_list)
    size = random.randrange(20, 100)
    xspeed = random.randrange(1, 10)
    yspeed = random.randrange(1, 10)
    new_ball = Ball(canvas, color, size, 500, 150, xspeed, yspeed)
    print(new_ball)             # 공(Ball 객체)의 정보 출력
    balls_list.append(new_ball) # 리스트에 공 추가

# 플레이어 유닛(Ball 객체) 생성
player = Ball(canvas)

# 메인 루프
while True:
    # 리스트에 저장된 포탄들을 이동시킴
    for bullet in bullets_list:
        try:
            bullet.move()
        except TclError:
            exit(0)    # 프로그램 종료 시 예외 처리

    # 리스트에 저장된 공들을 이동시킴
    for ball in balls_list:
        try:
            ball.move()
        except TclError:
            exit(0)    # 프로그램 종료 시 예외 처리

    window.update()     # 윈도우 출력 새로고침(변경된 값 반영)
    time.sleep(0.03)    # 0.03초 실행 지연