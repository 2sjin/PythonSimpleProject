A = int(input("First Data<int>: "))
B = float(input("Second Data<double>: "))

even = A % 2 == 0

if even:        # 첫 번째 입력이 짝수인 경우
    Result = 3 * B + 10
else:           # 첫 번째 입력이 홀수인 경우
    Result = 2 * B - 7

print(f"First Data={A}: even = {even}, Result = {Result}")

