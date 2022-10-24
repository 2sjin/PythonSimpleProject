import random

answer = random.randint(1, 100)    # 프로그램이 가지고 있는 정수(랜덤)
life = 8    # 입력 가능한 기회

print("숫자 게임에 오신 것을 환영합니다.")

while True:
    if life <= 0:   # 기회 8번 다 쓰면 실패
        print("…………")
        print("실패! 정답은", answer)
        break

    # 사용자가 입력한 정수
    inputed_num = int(input(f"({life}회 남음) 숫자를 맞춰 보세요: "))
    
    if inputed_num < answer:
        print("너무 작음!")
    elif inputed_num > answer:
        print("너무 큼!")
    else:
        print("…………")
        print("맞았음")
        break
    
    life -= 1   # 기회 1개 감소
    