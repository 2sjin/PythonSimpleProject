import numpy as np
import random
from tkinter import *

num_list = ["·", "１", "２", "３", "４", "５", "６", "７", "８", "　", "뒷면(지뢰)", "뒷면(안전)", "X표시(지뢰)", "X표시(안전)"]

fsize = 10       # 원하는 게임판 크기 설정
set_bomb = 10       # 원하는 지뢰 개수 설정
game_over = False     # 게임 오버 상태
bomb_count = 0       # 남은 지뢰 개수 카운트
bomb_start = 0         # 처음 지뢰 개수

win = Tk()
win.title("지뢰 빼고 다 찾기")
bomb_label = Label(win, text = '', font=("맑은 고딕", 30), fg = "red", bg = "yellow")
flabel_fontsize = 20
flabel = Label(win, text = '', font=("돋움체", flabel_fontsize))
l1 = Label(win, text = "게임 난이도")
e1 = Entry(win)
l2 = Label(win, text = "지뢰 수")
e2 = Entry(win)
e1.insert(0, str(fsize))
e2.insert(0, str(set_bomb))

# 재시작
def reset() :
    global game_over, bomb_count, bomb_start, field, bomb
    print("Reset the game.")
    game_over = False
    # 엔트리 입력 값 반영
    fsize = int(e1.get())
    set_bomb = int(e2.get())
    # 엔트리 값이 비정상적일 경우 강제로 변경
    if fsize < 10 :
        fsize = 10
    elif fsize > 20 :
        fsize = 20
        e1.delete(0, END)
        e1.insert(0, 20)
    # 출력 기호 초기화
    num_list[10] = "□"  # 뒷면(지뢰)
    num_list[11] = "□"  # 뒷면(안전)
    num_list[12] = "♧"  # X표시(지뢰)
    num_list[13] = "♧"  # X표시(안전)
    # 게임판 생성
    flist = []
    for i in range((fsize)**2) :
        flist.append(11)
    field = np.array(flist)
    field = field.reshape(fsize, fsize)
    # 지뢰 생성
    for i in range(set_bomb) : 
        bomb_a = random.randrange(0, fsize)
        bomb_b = random.randrange(0, fsize)
        field[bomb_a, bomb_b] = 10
    # 실제 지뢰 개수 계산
    bomb_count = 0
    for i in range(fsize) :
        for j in range(fsize) :
            if field[i, j] == 10 : 
                bomb_count += 1
    bomb_start = bomb_count
    if bomb_start != set_bomb :
        reset()
    # 게임판 갱신
    update_Label()

# 현재 좌표 구하기
def click_position(x, y) :
    c_row = int(y/(flabel_fontsize+8))
    c_column = int(x/(flabel_fontsize+8))
    return x, y, c_row, c_column

# 좌클릭 이벤트
def click_left(event) :
    global game_over, count
    if game_over == False :
        x, y, c_row, c_column = click_position(event.x, event.y)
        print("Click on " + str(x) + ", " + str(y) + ", " + str(c_row) + ", " + str(c_column))
        if c_row < fsize and c_column < fsize :
            if field[c_row, c_column] == 10 :
                print("Game over!")
                num_list[10] = "★"
                num_list[12] = "★"
                bomb_label['text'] = "GAME OVER"
                game_over = True
            elif field[c_row, c_column] != 12 and field[c_row, c_column] != 13 :
                explore(c_row, c_column)
            update_Label()

# 우클릭 이벤트
def click_right(event) :
    global bomb_count
    x, y, c_row, c_column = click_position(event.x, event.y)
    if field[c_row, c_column] == 10 :
        field[c_row, c_column] = 12
        bomb_count -= 1
    elif field[c_row, c_column] == 12 : 
        field[c_row, c_column] = 10
        bomb_count += 1
    elif field[c_row, c_column] == 11 : 
        field[c_row, c_column] = 13
        bomb_count -= 1
    elif field[c_row, c_column] == 13 : 
        field[c_row, c_column] = 11
        bomb_count += 1
    update_Label()

# 주변 지뢰 개수 확인
def explore(c_row, c_column):
    bomb_count = 0
    case_list = []
    if c_row > 0 :
        ftemp = field[c_row-1, c_column+0]
        case_list.append(ftemp == 10 or ftemp == 12)
        if c_column > 0 :
            ftemp = field[c_row-1, c_column-1]
            case_list.append(ftemp == 10 or ftemp == 12)
        if c_column < fsize-1 :
            ftemp = field[c_row-1, c_column+1]
            case_list.append(ftemp == 10 or ftemp == 12)
    if c_row < fsize-1 :
        ftemp = field[c_row+1, c_column+0]
        case_list.append(ftemp == 10 or ftemp == 12)
        if c_column > 0 :
            ftemp = field[c_row+1, c_column-1]
            case_list.append(ftemp == 10 or ftemp == 12)
        if c_column < fsize-1:
            ftemp = field[c_row+1, c_column+1]
            case_list.append(ftemp == 10 or ftemp == 12) 
    if c_column > 0 :
        ftemp = field[c_row+0, c_column-1]
        case_list.append(ftemp == 10 or ftemp == 12)
    if c_column < fsize-1 :
        ftemp = field[c_row+0, c_column+1]
        case_list.append(ftemp == 10 or ftemp == 12)    
    for k in case_list :
        if k == True:
            bomb_count += 1
    if field[c_row, c_column] != 10 and field[c_row, c_column] != 12 :
        field[c_row, c_column] = bomb_count
    return field[c_row, c_column]

# 게임판 갱신
def update_Label() :
    global field, bomb_count, bomb_label, flabel, game_over
    clear = game_clear()
    temp = ""
    for i in field :
        for j in i :
            temp += num_list[j]
        temp += "\n"
    if clear == False and game_over == False : 
        bomb_label['text'] = "★ " + str(bomb_count)
    flabel['text'] = temp

# 게임 완료 조건 확인
def game_clear() :
    global bomb_label, bomb_start, game_over
    clear_check = fsize**2
    for i in range(fsize) :
        for j in range(fsize) :
            if field[i, j] < 10 : 
                clear_check -= 1
    if clear_check <= bomb_start :
        bomb_label['text'] = "CLEAR"
        num_list[10] = "♧"
        num_list[12] = "♧"
        print("Clear!")
        game_over = False
        return True
    else :
        return False

# tkinter 실행
reset()
b1 = Button(win, text="다시하기", command=reset)
bomb_label.grid(row=0, column=0, columnspan = 2)
flabel.grid(row=1, column=0, columnspan = 2)
l1.grid(row = 2, column = 0)
e1.grid(row = 2, column = 1)
l2.grid(row = 3, column = 0)
e2.grid(row = 3, column = 1)
b1.grid(row = 4, column = 0, columnspan = 2)
update_Label()
flabel.bind("<Button-1>", click_left)
flabel.bind("<Button-3>", click_right)
win.mainloop()
