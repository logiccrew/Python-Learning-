# First
def greet():
    print("Hello!")

greet()

# Second
def Cal():

    operator = input("Enter operator (+, -, *, /): ")
    entries = int(input("How many numbers? "))

    numbers = []
    history = []

    i = 0
    while i < entries:
        num = int(input("Enter number: "))
        numbers.append(num)
        i += 1

    match operator:

        case "+":
            result = 0
            for n in numbers:
                result += n

        case "-":
            result = numbers[0]
            for n in numbers[1:]:
                result -= n

        case "*":
            result = 1
            for n in numbers:
                result *= n

        case "/":
            result = numbers[0]
            for n in numbers[1:]:
                result /= n if n != 0 else 1

        case _:
            result = "Invalid operator"

    print("Result:", result)
    history.append(result)

    return result


Cal()



    
