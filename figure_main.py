<<<<<<< HEAD
# %%
import figure
# [fill this line]

myline = figure.line(10, 20)

width, height = myline.get_length()

try:
    rectangle = figure.area_rectangle(width, height)
    print(rectangle)
except ValueError:
    print('please input positive number for width and height')

try:
    ellipse = figure.area_ellipse(width, height)
    print(ellipse)
except ValueError:
    print('please input positive number for width and height')

try:
    right_triangle = figure.area_right_triangle(width, height)
    print(right_triangle)
except ValueError:
    print('please input positive number for width and height')
=======
# %%
import figure
# [fill this line]

myline = figure.line(10)

square = figure.area_square(myline.get_length())
print(square)

myline.set_length(20)
regular_triangle = figure.area_regular_triangle(myline.get_length())
print(regular_triangle)

myline.set_length(30)
circle = figure.area_circle(myline.get_length())
print(circle)
>>>>>>> ca64f69e0fb635d7ef8d7cfabc4f4bbc11852f5a
