# 클래스
class Box:    
    # 생성자 : 멤버 변수는 private(__필드명)
    def __init__(self):        
        self.__width = 0
        self.__length = 0
        self.__height = 0
        print("Box 객체 생성됨")
    
    # 접근자(getter)
    def get_width(self):
        return self.__width

    def get_length(self):
        return self.__length

    def get_height(self):
        return self.__height
    
    # 설정자(setter)
    def set_width(self, value):
        self.__width = value

    def set_length(self, value):
        self.__length = value

    def set_height(self, value):
        self.__height = value
        
    # 메소드: 상자의 부피 리턴
    def get_scale(self):
        return self.__width * self.__length * self.__height
    
# 객체 생성
box = Box()

# setter 메소드 호출
box.set_width(100)
box.set_length(100)
box.set_height(100)

# getter 메소드 호출
print("상자 가로 :", box.get_width())
print("상자 세로 :", box.get_length())
print("상자 높이 :", box.get_height())

# 메소드 호출
print("상자 부피 =", box.get_scale())

