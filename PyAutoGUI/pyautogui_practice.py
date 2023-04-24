import pyautogui
import time

# 현재 마우스 포인터 좌표 알아내기
x, y = pyautogui.position()
print(x, y)

# 마우스 포인터 이동(절대 좌표)
pyautogui.moveTo(500, 500)

# 마우스 포인터 이동(상대 좌표)
# pyautogui.moveRel(500, 0, 2)

# 마우스 더블클릭
# pyautogui.click(clicks=2, interval=2)
pyautogui.doubleClick()

time.sleep(0.5)

# 글자 타이핑
pyautogui.typewrite("Hello World!")
pyautogui.typewrite(["space", "a", "b", "c", "enter"])
pyautogui.typewrite("PyAutoGUI")
