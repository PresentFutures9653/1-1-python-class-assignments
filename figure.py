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
