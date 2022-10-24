PAY = 1000  # 낸 돈(100원 고정)

while True:
    price = int(input("물건값을 입력하시오: "))
    if price < 1000:    # 1000원 미만일 경우
        break           # 입력 종료
    print("1000원 미만의 물건값을 입력하시오.")

change = PAY - price;   # 거스름돈

coin_value = (500, 100, 50, 10, 5, 1)   # 동전의 액면가

print("낸 돈:", PAY)
print("거스름돈: ", change, "\n")

for i in range(6):
    current_coin_count = change // coin_value[i]    # 동전 개수 계산
    change -= current_coin_count * coin_value[i]    # 동전 가격만큼 거스름돈 감소
    print(f"{coin_value[i]} 원 동전 개수: {current_coin_count}")
