import string

ALPHABET = string.ascii_lowercase   # 알파벳 소문자(a~z)
KEY = 3         # 암호키(알파벳 이동할 거리)


# 텍스트 파일 읽기 후, 읽어온 텍스트 데이터를 리턴하는 함수
def read_textfile(infile):
    result = ""
    
    line = infile.readline()        # 첫 줄 읽기
    while line != "":               # EOF를 만나면 읽기 종료
        result += line              # 읽기한 데이터 한 줄을 변수에 추가
        line = infile.readline()    # 다음 줄 읽기
        
    return result


# 암호화 함수
def enc(before):
    after = ""
    
    before = before.lower()       # 대문자는 모두 소문자로 변환

    # 평문을 1글자씩 확인
    for ch in before:
        ascii_code = ord(ch)    # 문자를 아스키 코드값으로 변환    
        if ch in ALPHABET:      # 문자가 알파벳이면
            ascii_code += KEY   # 암호화(키 값만큼 알파벳 오른쪽 이동)
            if ascii_code > ord("z"):   # 오버플로우 보정
                ascii_code -= 26        # 알파벳 개수인 26만큼 반대로 이동
    
        after += chr(ascii_code)   # 암호화한 문자를 암호문에 추가    
        
    return after


# 복호화 함수
def dec(before):
    after = ""
    
    before = before.lower()       # 대문자는 모두 소문자로 변환

    # 평문을 1글자씩 확인
    for ch in before:
        ascii_code = ord(ch)    # 문자를 아스키 코드값으로 변환    
        if ch in ALPHABET:      # 문자가 알파벳이면
            ascii_code -= KEY   # 복호화(키 값만큼 알파벳 왼쪽 이동)
            if ascii_code < ord("a"):   # 오버플로우 보정
                ascii_code += 26        # 알파벳 개수인 26만큼 역방향 이동
    
        after += chr(ascii_code)   # 암호화한 문자를 암호문에 추가    
        
    return after




print("*** 평문을 암호화하기 ***")

infile_1 = open("plain.txt", "r")       # 읽기 모드로 파일 열기
outfile_1 = open("cipher.txt", "w")     # 쓰기 모드로 파일 열기 

# 파일 내 데이터를 변수에 저장
str_in_file_1 = read_textfile(infile_1)
print("평문\n" + str_in_file_1)

# 암호화 후, 결과를 파일에 쓰기
cipher = enc(str_in_file_1)
outfile_1.write(cipher)
print("암호화 결과\n" + cipher + "\n")

# 파일 닫기
infile_1.close()
outfile_1.close()

print("\n*** 암호문을 복호화하기 ***")

infile_2 = open("cipher.txt", "r")        # 읽기 모드로 파일 열기
outfile_2 = open("decipher.txt", "w")     # 쓰기 모드로 파일 열기 

# 파일 내 데이터를 변수에 저장
str_in_file_2 = read_textfile(infile_2)
print("평문\n" + str_in_file_2)

# 복호화 후, 결과를 파일에 쓰기
decipher = dec(str_in_file_2)
outfile_2.write(decipher)
print("복호화 결과\n" + decipher + "\n")

# 파일 닫기
infile_2.close()
outfile_2.close()