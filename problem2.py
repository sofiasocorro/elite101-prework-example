'''PROBLEM 2: AREA CALCULATOR
Build an interactive area calculator that asks for a shape, requests the needed measurements, and handles invalid input gracefully.

'''

print("I can calculate the area of a shape for you. Which shape do you want me to calculate the area of?")

#ask for shape
while True:
    print('Please choose from the following shapes: circle, rectangle, square, or triangle: \n')
    shape = input('Shape: ')
    #UPPER/LOWER CASE + SPACE INSENSITIVE
    revised_output = shape.replace (" ", "").lower()
    pi = 3.14159
    
    #AREA FOR CIRCLE
    if revised_output == 'circle':
        radius = input('Please enter radius: ')
        radius = float(radius)
        area = (radius**2) * pi
        print('Area = ', area)
    
    #AREA FOR RECTANGLE
    if revised_output == 'rectangle':
        length = input('Please enter length: ')
        width = input('Please enter width: ')
        length = float(length)
        width = float(width)
        area = length * width
        print('Area = ', area)

    #AREA FOR SQUARE
    if revised_output == 'square':
        side = input('Please enter side length: ')
        side = float(side)
        area = side**2
        print('Area = ', area)

    #AREA FOR TRIANGLE
    if revised_output == 'triangle':
        base = input('Please enter base length: ')
        base = float(base)
        height = input('Please enter height: ')
        height = float(height)
        area = 1/2 * (base*height)
        print('Area = ', area)
