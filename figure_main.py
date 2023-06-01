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
    print(rectangle)
except ValueError:
    print('please input positive number for width and height')

try:
    rectangle = figure.area_right_triangle(width, height)
    print(rectangle)
except ValueError:
    print('please input positive number for width and height')