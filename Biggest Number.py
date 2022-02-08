print("Please choose 2 numbers")
number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))

if number1 > number2:
    print(number1)
elif number2 == number1:
    print("These numbers are equal")
else:
    print(number2)
