from email import message
from fileinput import filename
from tkinter import *
from tkinter import messagebox
from time import *

#############################################################################################

# 키 입력 시 이벤트 함수
def key_all(event):
    label_state.configure(text=f"키 [{chr(event.keycode)}] 입력")

# Shift+X 입력 시 이벤트 함수
def key_shift_x(event):
    app_exit()

# 왼쪽 키 입력 시 이벤트 함수
def key_left(event):
    go_prev_image()

# 오른쪽 키 입력 시 이벤트 함수
def key_right(event):
    go_next_image()

#############################################################################################

# 마우스 클릭 시 이벤트 함수
def mouse_all(event):
    txt=""
    if event.num == 1:
        txt += "좌클릭"
    elif event.num == 2:
        txt += "휠클릭"
    elif event.num == 3:
        txt += "우클릭"

    txt += f"({str(event.x)}, {str(event.y)})"  # 클릭한 좌표
    label_state.configure(text=txt)    

# 이미지를 마우스 좌클릭 시 이벤트 함수
def image_click(event):
    messagebox.showinfo("Image", f"현재 이미지: {filename_list[photo_page]}")

#############################################################################################

# 체크박스 선택 시 호출되는 함수
def func_cb():
    if chk.get() == 0:
        label_state.configure(text="체크 OFF")
    else:
        label_state.configure(text="체크 ON")

# 라디오박스 선택 시 호출되는 함수
def func_rb():
    if var.get() == 1:
        label_state.configure(text="파이썬 선택됨")
    elif var.get() == 2:
        label_state.configure(text="C++ 선택됨")
    elif var.get() == 3:
        label_state.configure(text="Java 선택됨")
    else:
        label_state.configure(text="Error")

#############################################################################################

# 프로그램 종료 함수
def app_exit():
    yes_or_no = messagebox.askyesno("Exit", "프로그램을 정말 종료하시겠습니까?")
    if yes_or_no == 1:  # [Yes] 선택 시
        quit()          # 프로그램 종료

# 이전 버튼 또는 해당 키 입력 시 호출되는 함수
def go_prev_image():
    global photo_page
    photo_page -= 1
    if photo_page < 0:
        photo_page = len(filename_list) - 1
    photo = PhotoImage(file="image/" + filename_list[photo_page])
    label_img.configure(image=photo)
    label_img.image = photo
    label_title.configure(text=filename_list[photo_page])

# 다음 버튼 또는 해당 키 입력 시 호출되는 함수
def go_next_image():
    global photo_page
    photo_page += 1
    if photo_page > len(filename_list) - 1:
        photo_page = 0
    image_load(PhotoImage(file="image/" + filename_list[photo_page]))

# 이미지 로드
def image_load(photo):
    label_img.configure(image=photo)
    label_img.image = photo
    label_title.configure(text=filename_list[photo_page])

#############################################################################################

# 데이터 저장
filename_list = ["jeju1.png", "jeju2.png", "jeju3.png"]
photo_list = [None] * len(filename_list)
photo_page = 0

#############################################################################################

# 윈도우 객체 생성 및 이미지 불러오기
window = Tk()

# 멤버 함수 호출을 통한 윈도우 속성 변경
window.title("제목 표시줄")
window.geometry("400x500")  # 윈도우 초기 크기
window.resizable(width=False, height=False) # 윈도우 창 크기 수동 조절 가능 여부

#############################################################################################

# 레이블 위젯(객체) 생성
label_state = Label(window, text="(null)", bg="magenta", anchor=SE)  # anchor=SE : 남동쪽(우하단)에 텍스트 정렬

# 레이블 위젯(객체) 생성
label_title = Label(window, text=filename_list[0], font=("궁서체", 20), fg="blue", bg="yellow")
photo = PhotoImage(file="image/" + filename_list[0])    # 이미지 출력
label_img = Label(window, image=photo, width=350, height=200)

# 버튼 위젯 생성
btn_quit = Button(window, text="파이썬 종료", fg="red", command=app_exit)
btn_prev = Button(window, text="<< 이전", fg="blue", command=go_prev_image)
btn_next = Button(window, text="다음 >>", fg="blue", command=go_next_image)

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

# 레이블 위젯 삽입
label_title.pack()
label_img.pack()
label_state.pack(fill=X, pady=5, ipady=10)    # 수평으로 늘리기

# 버튼 위젯 삽입: 수평으로 채우기, 외부 여백(pad), 내부 여백(ipad)
btn_prev.pack(side=LEFT, padx=10, pady=5, ipadx=20, ipady=10)          
btn_next.pack(side=LEFT, padx=10, pady=5, ipadx=20, ipady=10)
btn_quit.pack(side=RIGHT, padx=10, pady=5, ipadx=10, ipady=10)

# 체크박스 위젯 삽입: 고정 위치
cb1.place(x=25, y=310)

# 라디오버튼 위젯 삽입
i = 0
for rb in rb_list:
    rb.place(x=290, y=290+(i*24))
    i += 1

#############################################################################################

# 키보드 이벤트 처리
window.bind("<Key>", key_all)       # 아래 키들을 제외한 나머지 키 입력시 이벤트
window.bind("<Shift-X>", key_shift_x)      # Shift+X 입력 시 프로그램 종료
for key in ["<Left>", "<Up>"]:      # 이전 이미지 보기 이벤트를 적용할 키
    window.bind(key, key_left)      
for key in ["<Right>", "<Down>"]:   # 다음 이미지 보기 이벤트를 적용할 키
    window.bind(key, key_right)


# 마우스 이벤트 처리
window.bind("<Button>", mouse_all)        # 마우스 클릭 시 이벤트 
label_img.bind("<Button-1>", image_click)   # 이미지 내에서 마우스 좌클릭 시 이벤트

#############################################################################################

# 윈도우 출력
window.mainloop()

#############################################################################################