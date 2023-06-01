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
    