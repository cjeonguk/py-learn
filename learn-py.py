try:
    a = int(input("Enter a number: "))

except ValueError:
    print("You entered an invalid number")
    a = 0

finally:
    print("The number is: ", a)