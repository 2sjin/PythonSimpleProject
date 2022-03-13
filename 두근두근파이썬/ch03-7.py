import time     # time 모듈 불러오기

fseconds = time.time()  # 1970-01-01 00:00:00 부터 지금까지의 시간을 초로 환산
minute = int(fseconds // 60 % 60)     # 분 구하기
hour = int(fseconds // 3600 % 24)     # 시 구하기(서머타임 미적용)

print("현재 시각(영국 그리니치 시각): " + str(hour) + "시 " + str(minute) + "분") # 출력

