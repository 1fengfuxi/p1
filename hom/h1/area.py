import math

choice=input("please enter a shape that you wil like to caculate  enter in lower case and chose from one of the follwing shape circle square rectangle triangle ")
if choice=="circle":
    r = float(input("Enter the radius of a circle:"))
    area = math.pi * r * r
    print("Area of a circle "+str(+area))
elif choice=="triangle":
    height=float(input("enter the height "))
    base=float(input("enter the base please"))
    area=base*height/2
    print("area of triangle is "+str(area))
elif choice=="square":
    width=float(input("please enter the width of your square"))
    area=width*width
    print("area of squareis"+str(square))
    
else choice=="rectangle":
    width=float(input("please enter the width of your rectangle"))
    length=float(input("please enter you length of the rectangle"))
    area=width*width
    print("area of rectangle"+str(square))
