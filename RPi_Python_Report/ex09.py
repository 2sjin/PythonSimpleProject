import sys
from math import factorial

# 팩토리얼 연산(함수 재귀 호출)
def facto(end_num):
    if end_num > 1:
        return end_num * facto(end_num-1)
    else:
        return 1

# 팩토리얼을 곱셈 형태로 출력(예: 5! = (5*4*3*2*1))
def print_facto(end_num):
    # 끝 숫자가 2 이상이면 여는 괄호 출력
    if end_num > 1:
        print("(", end="")
    
    # 1부터 끝 숫자까지 숫자 출력
    for i in range(1, end_num+1):
        print(i, end="")
        if i < end_num:     # 끝 숫자가 아니면 곱셈 기호 출력
            print("*", end="")

    # 끝 숫자가 2 이상이면 여는 괄호 출력    
    if end_num > 1:
        print(")", end="")



# 첫 번째 명령행 인자를 정수로 변환하여 저장
num = int(sys.argv[1])

result = 0

print("\nResult = ", end="")

for i in range(1, num+1):
    result += facto(i)  # 팩토리얼 연산 결과를 결과에 합산함
    print_facto(i)      # 팩토리얼을 곱셈 형태로 출력
    
    # 마지막 부분이 아니면 덧셈 기호 출력
    if i < num:
        print(" + ", end="")

print(" =", result)