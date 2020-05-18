# Exercise 2. Odd and Even
#  - Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message
#    to the user.
#  - If the number is a multiple of 4, print out a different message.
#  - Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
#    If check divides evenly into num, tell that to the user. If not, print a different appropriate message.


num = int(input("Hello, please enter a number: "))
check = int(input("Enter a number to check: "))

if num % 4 == 0:
    print("Your number it's a multiple of 4")
elif num % 2 == 0:
    print("Your number it's even")
else:
    print("Your number it's odd")

if num % check == 0:
    print("And your number divides evenly into ", check)
else:
    print("And your number does not divide evenly into ", check)
