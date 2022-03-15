from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Calc")
window.geometry("350x190")

def key_input(value):
    print(value)
    if value.keysym in '0123456789':
        pressed_num(value.char)
    elif value.keysym == 'period':
        pressed_dot()
    elif value.keysym in ('plus', 'minus', 'asterisk', 'slash'):
        pressed_op(value.char)
    elif value.keysym in ('equal', 'Return'):
        get_result()
    elif value.keysym == 'Escape':
        reset()
    elif value.keysym == 'BackSpace':
        backspace()
    else:
        return

# 입력을 하였을 때 엔트리 초기화 여부
next_reset = True

# 함수: 숫자 버튼 눌렀을 때
def pressed_num(value):
    global next_reset
    if next_reset:
        entry.delete(0, "end")
    entry.insert("end", value)   # 엔트리의 끝부분에 입력한 숫자 추가
    next_reset = False

# 함수: 소수점(.) 버튼 눌렀을 때
def pressed_dot():
    global next_reset
    if entry.get() and entry.get()[-1].isdigit():
        entry.insert("end", '.')   # 엔트리의 끝부분에 입력한 숫자 추가
    next_reset = False

# 함수: 연산자 버튼 눌렀을 때
def pressed_op(op):
    global next_reset
    if entry.get()[-1].isdigit():
        get_result()
        next_reset = False
        entry.insert("end", f"{op}")   # 엔트리의 끝부분에 입력한 연산자 추가

# 함수: 연산 결과 출력
def get_result():
    global next_reset
    next_reset = True
    display = entry.get()
    if display == '':   # 공백 입력 시 무시
        return
    entry.delete(0, "end")   # 인덱스 0부터 끝까지 엔트리 문자열 제거
    try:
        entry.insert("end", eval(display))   # 엔트리의 끝부분에 입력한 숫자 추가
    except ZeroDivisionError:
        entry.insert("end", "0으로 나눌 수 없습니다.")
    except SyntaxError:
        return

# 함수: 초기화
def reset():
    global next_reset
    entry.delete(0, "end")   # 인덱스 0부터 끝까지 엔트리 문자열 제거
    entry.insert("end", '0')
    next_reset = True

# 함수: 한 칸 지우기
def backspace():
    entry.delete(len(entry.get())-1, "end")   # 인덱스 끝부분의 엔트리 문자열 제거
    if not entry.get():
        reset()

# 결과 표시창
entry_value = StringVar(window, value='')
entry = ttk.Entry(window, textvariable=entry_value, width=48)
entry.grid(row=0, column=0, columnspan=4, pady=10, ipady=5)     # 4열에 걸쳐서 출력

# 숫자 버튼
btn_7 = ttk.Button(window, text='7', command=lambda:pressed_num('7'))
btn_8 = ttk.Button(window, text='8', command=lambda:pressed_num('8'))
btn_9 = ttk.Button(window, text='9', command=lambda:pressed_num('9'))
btn_4 = ttk.Button(window, text='4', command=lambda:pressed_num('4'))
btn_5 = ttk.Button(window, text='5', command=lambda:pressed_num('5'))
btn_6 = ttk.Button(window, text='6', command=lambda:pressed_num('6'))
btn_1 = ttk.Button(window, text='1', command=lambda:pressed_num('1'))
btn_2 = ttk.Button(window, text='2', command=lambda:pressed_num('2'))
btn_3 = ttk.Button(window, text='3', command=lambda:pressed_num('3'))
btn_0 = ttk.Button(window, text='0', command=lambda:pressed_num('0'))
btn_7.grid(row=2, column=0)
btn_8.grid(row=2, column=1)
btn_9.grid(row=2, column=2)
btn_4.grid(row=3, column=0)
btn_5.grid(row=3, column=1)
btn_6.grid(row=3, column=2)
btn_1.grid(row=4, column=0)
btn_2.grid(row=4, column=1)
btn_3.grid(row=4, column=2)
btn_0.grid(row=5, column=0)

# 소수점 버튼
btn_dot = ttk.Button(window, text='.', command=pressed_dot)
btn_dot.grid(row=5, column=1)

# 연산자 버튼
btn_div = ttk.Button(window, text='/', command=lambda:pressed_op('/'))
btn_mul = ttk.Button(window, text='*', command=lambda:pressed_op('*'))
btn_sub = ttk.Button(window, text='-', command=lambda:pressed_op('-'))
btn_add = ttk.Button(window, text='+', command=lambda:pressed_op('+'))

btn_div.grid(row=2, column=3)
btn_mul.grid(row=3, column=3)
btn_sub.grid(row=4, column=3)
btn_add.grid(row=5, column=3)

# 기타 버튼
btn_equal = ttk.Button(window, text='=', command=get_result)
btn_AC = ttk.Button(window, text='AC', command=reset)
btn_back = ttk.Button(window, text='←', command=backspace)

btn_equal.grid(row=5, column=2)
btn_AC.grid(row=1, column=2)
btn_back.grid(row=1, column=3)

# 키 입력
window.bind("<Key>", key_input)

# 윈도우 출력
reset()
window.mainloop()