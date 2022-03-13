# tkenter 모듈의 모든 함수 포함
from tkinter import *

# 변환 함수
def process():
    inch_val = float(entry.get())            # 엔트리에 입력한 값을 실수로 변환하여 inch에 대입
    cm_val = inch_val * 2.54                 # inch(인치)에 2.54를 곱하여 cm(센티미터)에 대입
    l4['text'] = str(cm_val) + " 센티미터"   # 변환결과를 나타내는 레이블 갱신

# 최상위 윈도우 생성
window = Tk()

# 위젯 생성(레이블 4개, 엔트리 1개, 버튼 1개)
l1 = Label(window, text="인치를 센티미터로 변환하는 프로그램:")
l2 = Label(window, text="인치를 입력하시오: ")
l3 = Label(window, text="변환결과: ")
l4 = Label(window)
entry = Entry(window)
button = Button(window, text="변환!", command=process) # 버튼 클릭 시 함수 호출

# 격자 배치 관리자
l1.grid(row=0, column=0)
l2.grid(row=1, column=0)
l3.grid(row=2, column=0)
l4.grid(row=2, column=1)
entry.grid(row=1, column=1)
button.grid(row=3, column=1)

# 윈도우 이벤트 처리
window.mainloop()
