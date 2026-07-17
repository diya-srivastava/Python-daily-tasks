n = int(input("Enter a number: "))
factorial = 1
for i in range(1, 1+n):
    factorial *= i
print("The factorial of", n, "is", factorial)