
# Iterative version
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Recursive version
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

number = int(input("Enter a number: "))
print(f"Iterative factorial of {number} is {factorial_iterative(number)}")
print(f"Recursive factorial of {number} is {factorial_recursive(number)}")