# Writing a code in Python to find out the largest number among the given three numbers.
# The numbers are given input by the user.
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
if a > b and a > c:
    print(a, "is the largest number.")
elif b > a and b > c:
    print(b, "is the largest number.")
else:
    print(c, "is the largest number.")
