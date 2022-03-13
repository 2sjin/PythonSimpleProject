# tkinter 모듈의 모든 함수 포함
from tkinter import *

# 더하기 함수
def add() :
    global total                 # total(합계) 변수를 전역 변수로 사용
    add = int(entry.get())       # 엔트리에 입력한 값을 정수로 변환하여 add에 대입
    total += add                 # total(합계)에 add를 더함
    l2['text'] = str(total)      # 합계를 나타내는 레이블 갱신

# 빼기 함수
def subtract() :
    global total                 # total(합계) 변수를 전역 변수로 사용
    subtract = int(entry.get())  # 엔트리에 입력한 값을 정수로 변환하여 subtract에 대입
    total -= subtract            # total(합계)에 subtract를 더함
    l2['text'] = str(total)      # 합계를 나타내는 레이블 갱신

# 초기화 함수
def reset() :
    global total                 # total(합계) 변수를 전역 변수로 사용
    total = 0                    # total(합계)
    l2['text'] = str(total)      # 합계를 나타내는 레이블 갱신

# 최상위 윈도우 생성
window = Tk()

# 위젯 생성(레이블 2개, 엔트리 1개, 버튼 3개)
l1 = Label(window, text="현재 합계: ")
l2 = Label(window, text="'초기화' 클릭!")      # 최초 실행 후 '초기화' 단추 클릭하라는 레이블 출력
entry = Entry(window)
b1 = Button(text="더하기(+)", command=add)     # 버튼 클릭 시 더하기 함수 호출
b2 = Button(text="빼기(-)", command=subtract)  # 버튼 클릭 시 빼기 함수 호출
b3 = Button(text="초기화", command=reset)      # 버튼 클릭 시 초기화 함수 호출

# 격자 위치 배치 관리자
l1.grid(row=0, column=0)
l2.grid(row=0, column=1, columnspan=2)      # 0행 1열 기준으로 2개의 열을 합침
entry.grid(row=1, column=0, columnspan=3)   # 1행 0열 기준으로 3개의 열을 합침
b1.grid(row=2, column=0) 
b2.grid(row=2, column=1)
b3.grid(row=2, column=2)


# 윈도우 이벤트 처리
window.mainloop()
