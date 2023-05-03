import math

exercises = 0

while exercises < 99:

    exercises = int(input("Enter the number of the exercise you want to run: "))

    if exercises == 1:
        base = float(input("Enter the base measurement of the triangle: "))
        height = float(input("Enter the height measurement of the triangle: "))
        print("The value of the area is", (base * height) / 2)
    elif exercises == 2:
        firstNumber = float(input("Enter the first number: "))
        secondNumber = float(input("Enter the second number: "))
        print("The sum of the numbers is", firstNumber + secondNumber)
    elif exercises == 3:
        number = float(input("Enter the number: "))
        print("The number", number, "raised to the square is", math.pow(number, 2))
    elif exercises == 4:
        print("The sum of the numbers 1234 and 532 is", 1234+532)
    elif exercises == 5:
        print("The subtraction of the numbers 1234 and 532 is", 1234-532)
    elif exercises == 6:
        print("The multiplication of the numbers 1234 and 532 is", 1234*532)
    elif exercises == 7:
        print("The division of the numbers 1234 and 532 is", 1234/532)
    elif exercises == 8:
        print("The module of the numbers 1234 and 532 is", 1234%532)
    elif exercises == 9:
        euro = float(input("Enter the value in euros: "))
        print(euro, "euros are equivalent to", euro*1.10, "dollars")
    elif exercises == 10:
        base = float(input("Enter the width measurement of the rectangle: "))
        height = float(input("Enter the height measurement of the rectangle: "))
        print("The value of the area of the rectangle is", base * height)
    elif exercises == 11:
        side = float(input("Enter the measure of the side of the square: "))
        print("The area of this square is", math.pow(side, 2))
        print("The perimeter of this square is", side * 4)
    elif exercises == 12:
        radius = float(input("Enter the radius measurement of the cylinder: "))
        height = float(input("Enter the height measurement of the cylinder: "))
        print("The value of the area of the cylinder is", (2 * math.pi * radius * height) + (2 * math.pi * math.pow(radius, 2)))
        print("The value of the volume of the cylinder is", math.pi * math.pow(radius, 2) * height)
    elif exercises == 13:
        radius = float(input("Enter the radius measurement of the circumference: "))
        print("The value of the length of the circle is", (radius * 2) * math.pi)
        print("The value of the area of the circle is", math.pow(radius, 2) * math.pi)
    elif exercises == 14:
        firstNumber = float(input("Enter the value of the first number: "))
        secondNumber = float(input("Enter the value of the second number: "))
        thirdNumber = float(input("Enter the value of the third number: "))
        print("The average between these three numbers is", (firstNumber + secondNumber + thirdNumber) / 3)
    elif exercises == 15:
        firstNumerator = float(input("Enter the numerator of the first fraction: "))
        firstDenominator = float(input("Enter the denominator of the first fraction: "))
        secondNumerator = float(input("Enter the numerator of the second fraction: "))
        secondDenominator = float(input("Enter the denominator of the second fraction: "))
        sumNumerator = firstNumerator * secondDenominator + secondNumerator * firstDenominator
        sumDenominator = firstDenominator * secondDenominator
        print("The sum of the fractions is equal to", sumNumerator, "/", sumDenominator)
    elif exercises == 16:
        firstNumber = float(input("Enter the first number: "))
        secondNumber = float(input("Enter the second number: "))
        print("The number", firstNumber, "raised to the", secondNumber, "is equal to", math.pow(firstNumber, secondNumber))
