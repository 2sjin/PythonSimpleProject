from tkinter import *
from tkinter import messagebox
from time import *

#############################################################################################

# 사용자 정의 함수 모음

# 체크박스 선택 시
def func_cb():
    if chk.get() == 0:
        messagebox.showinfo("Title: CheckBox", "체크 OFF")
    else:
        messagebox.showinfo("Title: CheckBox", "체크 ON")

# 라디오박스 선택 시
def func_rb():
    if var.get() == 1:
        label_state.configure(text="파이썬 선택됨")
    elif var.get() == 2:
        label_state.configure(text="C++ 선택됨")
    elif var.get() == 3:
        label_state.configure(text="Java 선택됨")
    else:
        label_state.configure(text="Error")

# 이전 버튼 클릭 시
def click_prev_image():
    global num
    num -= 1
    if num < 0:
        num = len(filename_list) - 1
    photo = PhotoImage(file="image/" + filename_list[num])
    label_img.configure(image=photo)
    label_img.image = photo
    label_title.configure(text=filename_list[num])

# 다음 버튼 클릭 시
def click_next_image():
    global num
    num += 1
    if num > len(filename_list) - 1:
        num = 0
    image_load(PhotoImage(file="image/" + filename_list[num]))

# 이미지 로드
def image_load(photo):
    label_img.configure(image=photo)
    label_img.image = photo
    label_title.configure(text=filename_list[num])

#############################################################################################

# 데이터 저장
filename_list = ["jeju1.png", "jeju2.png", "jeju3.png"]
photo_list = [None] * len(filename_list)
num = 0

#############################################################################################

# 윈도우 객체 생성 및 이미지 불러오기
window = Tk()

# 멤버 함수 호출을 통한 윈도우 속성 변경
window.title("제목 표시줄")
window.geometry("400x500")  # 윈도우 초기 크기
window.resizable(width=False, height=False) # 윈도우 창 크기 수동 조절 가능 여부

#############################################################################################

# 레이블 위젯(객체) 생성
label_state = Label(window, text="공부 중입니다.", bg="magenta", anchor=SE)  # anchor=SE : 남동쪽(우하단)에 텍스트 정렬

# 레이블 위젯(객체) 생성
label_title = Label(window, text=filename_list[0], font=("궁서체", 20), fg="blue", bg="yellow")
photo = PhotoImage(file="image/" + filename_list[0])    # 이미지 출력
label_img = Label(window, image=photo, width=350, height=200)

# 버튼 위젯 생성
btn_quit = Button(window, text="파이썬 종료", fg="red", command=quit)
btn_prev = Button(window, text="<< 이전", fg="blue", command=click_prev_image)
btn_next = Button(window, text="다음 >>", fg="blue", command=click_next_image)

# 체크박스 위젯 생성
chk = IntVar()  # 체크박스 상태를 저장할 변수  
cb1 = Checkbutton(window, text="클릭하세요", variable=chk, command=func_cb)

# 라디오버튼 위젯 생성
var = IntVar()  # 라디오박스 상태를 저장할 변수
rb_list = [None] * 3                # 라디오박스 리스트
rb_text = ["파이썬", "C++", "Java"]  # 라디오박스 텍스트 리스트
for i in range(3):
    rb_list[i] = Radiobutton(window, text=rb_text[i], variable=var, value=i+1, command=func_rb)

#############################################################################################

# 레이블 위젯 적용
label_title.pack()
label_img.pack()
label_state.pack(fill=X, pady=5, ipady=10)    # 수평으로 늘리기

# 버튼 위젯 적용: 수평으로 채우기, 외부 여백(pad), 내부 여백(ipad)
btn_prev.pack(side=LEFT, padx=10, pady=5, ipadx=20, ipady=10)          
btn_next.pack(side=LEFT, padx=10, pady=5, ipadx=20, ipady=10)
btn_quit.pack(side=RIGHT, padx=10, pady=5, ipadx=10, ipady=10)

# 체크박스 위젯 적용: 고정 위치
cb1.place(x=25, y=310)

# 라디오버튼 위젯 적용
i = 0
for rb in rb_list:
    rb.place(x=290, y=290+(i*24))
    i += 1

#############################################################################################

# 윈도우 출력
window.mainloop()