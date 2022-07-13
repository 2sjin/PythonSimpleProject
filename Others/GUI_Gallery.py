#############################################################################################

import os

from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
from tkinter.simpledialog import *

#############################################################################################

# 허용 확장자
FILE_TYPES = (("PNG 파일", "*.png"), ("GIF 파일", "*.gif"), ("JPG 파일", "*.jpg"), ("모든 파일", "*.*"))

WINDOW_SIZE = (400, 500)
IMAGE_DIR = "image/"    # 이미지 디렉토리

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
        label_state.configure(text="체크박스 OFF")
    else:
        label_state.configure(text="체크박스 ON")

# 라디오박스 선택 시 호출되는 함수
def func_rb():
    if var.get() == 1:
        label_state.configure(text="라디오버튼 A 선택됨")
    elif var.get() == 2:
        label_state.configure(text="라디오버튼 B 선택됨")
    elif var.get() == 3:
        label_state.configure(text="라디오버튼 C 선택됨")
    else:
        label_state.configure(text="Error")

#############################################################################################

# 파일 열기 함수
def file_open():
    opened_file = askopenfilename(parent=window, filetypes=FILE_TYPES)
    if opened_file != "":     # 파일 탐색기를 취소하지 않을 경우에만 새 이미지 로드
        image_load(PhotoImage(file=opened_file))
        label_title.configure(text=opened_file.split("/")[-1])
        window.title(opened_file.split("/")[-1])

# 프로그램 종료 함수
def app_exit():
    yes_or_no = messagebox.askyesno("Exit", "프로그램을 정말 종료하시겠습니까?")
    if yes_or_no == 1:  # [Yes] 선택 시 프로그램 종료
        window.quit()
        window.destroy()
        exit()

#############################################################################################

# 이전 버튼 또는 해당 키 입력 시 호출되는 함수
def go_prev_image():
    global photo_page
    photo_page -= 1
    if photo_page < 0:
        photo_page = len(filename_list) - 1
    image_load(PhotoImage(file=IMAGE_DIR + filename_list[photo_page]))
    window.title(filename_list[photo_page])

# 다음 버튼 또는 해당 키 입력 시 호출되는 함수
def go_next_image():
    global photo_page
    photo_page += 1
    if photo_page > len(filename_list) - 1:
        photo_page = 0
    image_load(PhotoImage(file=IMAGE_DIR + filename_list[photo_page]))
    window.title(filename_list[photo_page])

# 이미지 로드
def image_load(photo):
    label_img.configure(image=photo)
    label_img.image = photo
    label_title.configure(text=filename_list[photo_page])

#############################################################################################

# 데이터 저장
extension_list = tuple([FILE_TYPES[i][1].replace('*', '') for i in range(len(FILE_TYPES)-1)])   # 확장자 튜플
filename_list = file_list = [f for f in os.listdir(IMAGE_DIR) if f.endswith(extension_list)]
photo_list = [None] * len(filename_list)
photo_page = 0

#############################################################################################

# 윈도우 객체 생성 및 이미지 불러오기
window = Tk()

# 멤버 함수 호출을 통한 윈도우 속성 변경
window.title(filename_list[0])
window.geometry(f"{WINDOW_SIZE[0]}x{WINDOW_SIZE[1]}")  # 윈도우 초기 크기
window.resizable(width=False, height=False) # 윈도우 창 크기 수동 조절 가능 여부

#############################################################################################

# 메뉴 생성
mainMenu = Menu(window)         # 메뉴 객체 생성
window.config(menu=mainMenu)    # 윈도우에 메뉴 추가

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)   # 상위 메뉴 생성
fileMenu.add_command(label="파일 열기", command=file_open)  # 하위 메뉴 생성
fileMenu.add_separator()            # 구분선 생성
fileMenu.add_command(label="프로그램 종료", command=app_exit)  # 하위 메뉴 생성

#############################################################################################

# 레이블 위젯(객체) 생성
label_state = Label(window, text="(null)", bg="magenta", anchor=SE)  # anchor=SE : 남동쪽(우하단)에 텍스트 정렬

# 레이블 위젯(객체) 생성
label_title = Label(window, text=filename_list[0], font=("맑은 고딕", 15), fg="blue", bg="white")
photo = PhotoImage(file=IMAGE_DIR + filename_list[0])    # 이미지 출력
label_img = Label(window, image=photo, width=350, height=200)

# 버튼 위젯 생성
btn_quit = Button(window, text="프로그램 종료", fg="red", command=app_exit)
btn_prev = Button(window, text="<< 이전", fg="blue", command=go_prev_image)
btn_next = Button(window, text="다음 >>", fg="blue", command=go_next_image)

# 체크박스 위젯 생성
chk = IntVar()  # 체크박스 상태를 저장할 변수  
cb1 = Checkbutton(window, text="CheckBox", variable=chk, command=func_cb)

# 라디오버튼 위젯 생성
var = IntVar()  # 라디오박스 상태를 저장할 변수
rb_list = [None] * 3                # 라디오박스 리스트
rb_text = ["Radio A", "Radio B", "Radio C"]  # 라디오박스 텍스트 리스트
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
