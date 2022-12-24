from art import logo

print(logo)


def adding(number1, number2):
    result = number1 + number2
    print(f"{number1} + {number2} = {result}")
    return result


def multiplying(number1, number2):
    result = number1 * number2
    print(f"{number1} * {number2} = {result}")
    return result


def extraction(number1, number2):
    result = number1 - number2
    print(f"{number1} - {number2} = {result}")
    return result


def dividing(number1, number2):
    result = number1 / number2
    print(f"{number1} / {number2} = {result}")
    return result


def process(number1, number2):
    process1 = input("Pick an operation: \n"
                     "*\n"
                     "+\n"
                     "-\n"
                     "/\n")
    if process1 == "*":
        result = multiplying(number1, number2)
        return result
    elif process1 == "+":
        result = adding(number1, number2)
        return result
    elif process1 == "/":
        result = dividing(number1, number2)
        return result
    elif process1 == "-":
        result = extraction(number1, number2)
        return result
    else:
        print("You typed invalid symbol. Please try again.")


def main():
    number1 = int(input("What is the first number? : \n"))
    number2 = int(input("What is the second number? : \n"))
    result = process(number1, number2)
    continuee = input(f"Do you want to continue calculating with {result}: \n")
    while continuee in "Yy":
        new_number = int(input("Please write a new number:"))
        result = process(new_number, result)
        continuee = input(f"Do you want to continue calculating with: {result} \n")
        if continuee not in "yY":
            break


main()

while True:
    pass
