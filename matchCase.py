# First problem

print("Enter your command to execute the System.\nCommands are:\nStart\nEnd\nContinue\nStop")
messgae =str(input("Enter your command :"))

match messgae.lower():
    case "start":
        print("System starting...")
    case "end":
        print("System ending...")
    case "continue":
        print("System continue...")
    case "stop":
        print("System stop...")
    case _:
        print("Unknown command. Please use Start, End, Continue, or Stop.")

# Second problem

print("Enter your measumerments to Calculate the Area and also select the shape which you want to calculate the area.\n Shapes are:\nCircle \nTriangle\nSquare\nRectangle")
shape =str(input("Enter your shape :"))

match shape.lower():
    case "circle":
        radius = float(input("Enter your radius :"))
        area = 3.14 * radius**2
        print("Area of Circle :",area) 
    case "triangle":
        base = float(input("Enter your base :"))
        height = float(input("Enter your height :"))
        area = 0.5 * base * height
        print("Area of Triangle :",area) 
    case "rectangle":
        len =float(input("Enter your len :"))
        width =float(input("Enter your width :"))
        area = len * width
        print("Area of Rectangle :",area) 

    case "square":
        len =float(input("Enter your len :"))
       
        area = 4*len
        print("Area of Square :",area) 
    case _:
        print("Unknown command. Please use Start, End, Continue, or Stop.")

