# random 모듈 가져오기
import random

# [1 횟수, 2 횟수, 3 횟수, 4 횟수, 5 횟수, 6 횟수]
counters = [0, 0, 0, 0, 0, 0]

# 아래 과정을 1000회 반복
for i in range(1000) :
    dice = random.randint(1,6)  # 주사위 던지기
    for i in range(6) :         
        if dice == i + 1 :      # 주사위 1~6 값이 주사위 값과 일치하면  
            counters[i] += 1    # counters[0~5]에 1을 더한다. 

# 주사위가 1~6인 경우는 각각 몇 번인지 출력
# 예를 들어, 주사위가 3(2+1)인 경우는 counters[2]의 값
for i in range(6) : 
    print("주사위가", i+1, "인 경우는", counters[i])
