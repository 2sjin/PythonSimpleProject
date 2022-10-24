# A+ : 95 이상    # A0 : 90 이상    # B+ : 85 이상    # B0 : 80 이상
# C+ : 75 이상    # C0 : 70 이상    # D+ : 65 이상    # D0 : 60 이상    # F : 60 미만

def score_to_grade(score):
    tenth_digit = score // 10   # 점수의 십의 자리
    first_digit = score % 10    # 점수의 일의 자리
    
    if score < 0 or score > 100:  # 점수 범위를 벗어남
        return "E"                  # ERROR를 의미
    
    elif score == 100:    # 100점
        return "A+"
        
    elif score < 60:    # 60점 미만
        return "F"
    
    # 딕셔너리: 십의 자리(key)에 따른 등급 알파벳(value)
    dic_score = {9:"A", 8:"B", 7:"C", 6:"D"}
    
    result = ""
    for key, value in dic_score.items():
        if tenth_digit == key:  # 십의 자리(key)에 따라
            result += value      # 해당하는 등급 알파벳(value)가 부여됨
            break
            
    if first_digit >= 5:    # 일의 자리가 5 이상이면
        result += "+"       # '+' 등급
    else:                   # 5 미만이면
        result += "0"       # '0' 등급
        
    return result


grade = "E"
while grade == "E":   # 정상적인 점수가 입력될 때 까지 반복
    score = float(input("성적 값을 입력 하시오(0.0 ~ 100.0): "))
    grade = score_to_grade(score)

print(f"당신의 학점은 {grade} 입니다.")



