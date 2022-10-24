import sys

A = int(sys.argv[1])     # 첫 번째 명령행 인자를 정수로 변환하여 저장

result_sum = 0
result_stdout = "sum = ("

infile = open("Input.txt", "r")       # 읽기 모드로 파일 열기
outfile = open("Result.txt", "w")     # 쓰기 모드로 파일 열기 

first_line = infile.readline()          # 첫 줄의 데이터 읽기
B, C = map(int, first_line.split())     # 띄어쓰기로 두 정수를 분리함

print(f"A={A}, B={B}, C={C}\n")

for i in range(B, C+1):
    result_sum += i
    result_stdout += str(i)
    if i < C:                   # 마지막 수가 아닐 경우
        result_stdout += " + "  # 덧셈 기호 출력
    
result_stdout += ")"

result_sum += A
result_stdout += f" + {A} = {result_sum}"


# 출력 결과를 파일 쓰기
outfile.write(result_stdout)
print(result_stdout)

# 파일 닫기
infile.close()
outfile.close()
