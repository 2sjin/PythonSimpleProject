from sys import stdin

# TV 클래스
class TV:

    # 생성자
    def __init__(self, ch=1, vol=0):
        self.channel = 1
        self.volume = 0
        self.power = False
        print(f"TV 객체 생성(채널 {self.channel}, 음량 {self.volume})")

    # __str__ 메소드(TV 정보 출력)
    def __str__(self):
        if self.power:
            return f"TV의 채널: {self.channel}, TV의 음량: {self.volume}"
        else:
            return f"(TV 꺼짐)"

    # TV를 켜는 함수
    def turnOn(self):
        self.power = True

    # TV를 끄는 함수
    def turnOff(self):
        self.power = False

    # 채널을 변경하는 함수
    def setChannel(self, ch):
        if self.power:
            self.channel = ch

    # 볼륨을 변경하는 함수
    def setVolume(self, vol):
        if self.power:
            self.volume = vol

# TV 객체 생성
tv = TV()

# 명령 반복
while True:
    cmd = stdin.readline().strip()

    # TV 켜기
    if cmd[:2] == "on":
        tv.turnOn()

    # TV 끄기
    elif cmd[:3] == "off":
        tv.turnOff()

    # 채널 변경(0~999)
    elif cmd.isdigit():
        tv.setChannel(int(cmd[0:3]))

    # 볼륨 변경(0~99)
    elif cmd[:1] == "v":
        tv.setVolume(int(cmd[1:3]))

    # TV 정보 표시        
    print(tv)
