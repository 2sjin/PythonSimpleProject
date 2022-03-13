# 빈 딕셔너리 생성
contacts = {}

# name 값 입력 없이 Enter 키를 누를 때마다 입력 모드와 검색 모드 전환(Toggle)
while True:
    
    # 입력 모드
    while True:
        name = input("(입력모드) 이름을 입력하시오: ")
        if not name: 
            break;      # name 값을 입력하지 않으면 검색모드로 변경
        tel = input("전화번호를 입력하시오: ")
        contacts[name] = tel    # 딕셔너리에 키(name)-값(tel) 쌍 추가

    # 검색 모드
    while True:
        name = input("(검색모드) 이름을 입력하시오: ")
        if not name: 
            break;      # name 값을 입력하지 않으면 입력모드로 변경
        if name in contacts : 
            print(name, "의 전화번호는", contacts[name], "입니다.") # 이름, 전화번호 출력
        else :
            print(name, "의 정보가 없습니다.")   # 딕셔너리에 없는 이름의 출력
