class Shape:
    def __init__(self, area, perimeter):

        self.area = area
        self.perimeter = perimeter

        return self


class quadrilateral(Shape):
        pass


class square(quadrilateral):

            def area():
                x = int(input("Please enter the length of one side of the square:"))

                return x * x

            def perimeter():
                x = int(input("Please enter the length of one side of the square:"))

                return 4 * x


class rectangle(quadrilateral):
    def area():
        x = int(input("Please enter the length of the rectangle:"))
        y = int(input("Please enter the width of the rectangle:"))

        return x*y

    def perimeter():
        x = int(input("Please enter the length of the rectangle:"))
        y = int(input("Please enter the width of the rectangle:"))
        return 2*(x+y)


class circle(Shape):
        def area():
            x = int(input("Please enter the radius of the circle:"))
            return 3.14*x*x

        def perimeter():
            x = int(input("Please enter the radius of the circle:"))
            return 2*3.14*x


class triangle(Shape):
    def area():
        x = int(input("Please enter the base of the triangle:"))
        y = int(input("Please enter the height of the triangle:"))
        return int(.5*x*y)

    def perimeter():
        x = int(input("Please enter the length of one side one of the triangle:"))
        y = int(input("Please enter the length of the next side one of the triangle:"))
        z = int(input("Please enter the length of the last side one of the triangle:"))
        return x + y + z


shape = input("What is the shape for which you'd like to calculate area or perimeter? (square, rectangle, circle, or triangle):  ")
shape = shape.lower()

calculation = input("Would you like to calculate area or perimeter of the {}?:".format(shape))
calculation = calculation.lower()

if shape == "square" and calculation == "area":
    print("The {} of the {} is {}".format(calculation, shape, square.area()))
if shape == "square" and calculation == "perimeter":
    print("The {} of the {} is {}".format(calculation, shape, square.perimeter()))
if shape == "rectangle" and calculation == "area":
    print("The {} of the {} is {}".format(calculation, shape, rectangle.area()))
if shape == "rectangle" and calculation == "perimeter":
    print("The {} of the {} is {}".format(calculation, shape, rectangle.perimeter()))
if shape == "circle" and calculation == "area":
    print("The {} of the {} is {}".format(calculation, shape, circle.area()))
if shape == "circle" and calculation == "perimeter":
    print("The {} of the {} is {}".format(calculation, shape, circle.perimeter()))
if shape == "triangle" and calculation == "area":
    print("The {} of the {} is {}".format(calculation, shape, triangle.area()))
if shape == "triangle" and calculation == "perimeter":
    print("The {} of the {} is {}".format(calculation, shape, triangle.perimeter()))
