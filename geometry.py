# This program contains functions that evaluate formulas used in geometry.
#
# Kenneth Alexander
# August 31, 2017

import math

def triangle_area(b, h):
    a = (1/2) * b * h
    return a

def circle_area(r):
    a = math.pi * r**2
    return a

# function calls
print(triangle_area(4,9))
print(circle_area(5))
print(circle_area(12))

def parallelogram_area(b, h):
    a= b * h
    return a
# function calls
print(parallelogram_area(5,9))

def trapezoid_area(a, b, h):
    A=(a + b)/2 * h
    return A
# function calls
print(trapezoid_area(4,6,8))

def rectangular_prism_volume(l, w, h):
    v=l*w*h
    return v
# function calls
print(rectangular_prism_volume(5, 7, 9))

def cone_volume(r, h):
    v= math.pi * r**2 *(h/3)
    return v
#functin calls
print(cone_volume(5, 9))

def sphere_volume(r):
    v= (4/3) * math.pi * r**3
    return v
# function calls
print(sphere_volume(4))

def rectangular_prism_area(w, l, h):
    a= 2*(w*l+h*l+h*w)
    return a
#function calls
print(rectangular_prism_area(4, 5, 8))

def sphere_area(r):
    a= 4 * math.pi * r**3
    return a
#function calls
print(sphere_area(4))

def triangle_hypotenuse(a, b):
    c= a**2 + b**2
    return c
#function calls
print(triangle_hypotenuse(5,6))
