<<<<<<< HEAD
import math

# 도형 높이. 너비 클래스
class line:

    __width = 0
    __height = 0

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def set_length(self, width, height):  # setter
        self.__width = width
        self.__height = height

    def get_length(self):  # getter
        return self.__width, self.__height
    



# 높이, 너비 받아 직사각형 넓이 반환
def area_rectangle(width, height):
       
    if width <= 0 or height <= 0:
        raise ValueError
    
    return width * height


# 높이, 너비 받아 타원 넓이 반환.
def area_ellipse(width, height):

    if width <= 0 or height <= 0:
        raise ValueError
    
    return width * height * math.pi


# 높이, 너비 받아 직각삼각형 넓이 반환.
def area_right_triangle(width, height):
  
    if width <= 0 or height <= 0:
            raise ValueError
    
    return (width * height) / 2
    
=======
import math

# 선분 길이 클래스
class line:
    def __init__(self, length=0):
        self.__length = length

    def set_length(self, length):  # setter
        self.__length = length

    def get_length(self):  # getter
        return self.__length


# 선분의 길이를 받아 한 변 길이로 취급, 정사각형 넓이 반환.
def area_square(length):
    return length ** 2


# 선분의 길이를 받아 반지름으로 취급, 원 넓이 반환.
def area_circle(length):
    return (length ** 2) * math.pi


# 선분의 길이를 받아 한 변 길이로 취급, 정삼각형 넓이 반환.
def area_regular_triangle(length):
    return (math.sqrt(3) / 4) * (length ** 2)
>>>>>>> ca64f69e0fb635d7ef8d7cfabc4f4bbc11852f5a
