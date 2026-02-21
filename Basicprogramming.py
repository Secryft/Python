"""
Python Practice Exercises
Author: Aditya
Description: Basic Python exercises covering arithmetic logic,
loops, strings, and factorial calculation.
"""

# ---------------------------------------------------------
# Exercise 1: Arithmetic Product and Conditional Logic
# ---------------------------------------------------------
def product(number1, number2):
    """
    Multiply two numbers.
    If result <= 1000 → print product
    Else → print sum of numbers
    """
    result = number1 * number2
    if result <= 1000:
        print("The result is:", result)
    else:
        print("The result is:", number1 + number2)


# ---------------------------------------------------------
# Exercise 2: Cumulative Sum of Range (0–9)
# ---------------------------------------------------------
def cumulative_sum():
    """
    Print current number, previous number,
    and their sum for range(10)
    """
    print("\nPrinting current and previous number sum in a range(10)")
    previous_number = 0

    for current_number in range(10):
        total = current_number + previous_number
        print(
            "Current Number", current_number,
            "Previous Number", previous_number,
            "Sum:", total
        )
        previous_number = current_number


# ---------------------------------------------------------
# Exercise 3: Print characters at even index positions
# ---------------------------------------------------------
def even_index_chars(text):
    """Print characters present at even index positions"""
    print("\nEven index characters:")
    for i in range(len(text)):
        if i % 2 == 0:
            print(text[i])


# ---------------------------------------------------------
# Exercise 4: Remove first n characters from string
# ---------------------------------------------------------
def remove_chars(text, n):
    """Remove first n characters from a string"""
    print("\nString after removing first", n, "chars:", text[n:])


# ---------------------------------------------------------
# Extra: Swap numbers using temp variable
# ---------------------------------------------------------
def swap_with_temp(a, b):
    temp = a
    a = b
    b = temp
    print("\nSwap using temp:", a, b)


# ---------------------------------------------------------
# Extra: Swap numbers without temp variable
# ---------------------------------------------------------
def swap_without_temp(a, b):
    a = a + b
    b = a - b
    a = a - b
    print("Swap without temp:", a, b)


# ---------------------------------------------------------
# Exercise 5: Factorial of a number
# ---------------------------------------------------------
def factorial(num):
    """Calculate factorial of a number"""
    product = 1
    for i in range(1, num + 1):
        product = product * i
    print("\nFactorial of", num, "is:", product)


# ---------------------------------------------------------
# Main function
# ---------------------------------------------------------
if __name__ == "__main__":
    product(20, 30)
    product(40, 30)

    cumulative_sum()

    even_index_chars("pynative")

    remove_chars("pynative", 4)
    remove_chars("pynative", 2)

    swap_with_temp(5, 10)
    swap_without_temp(5, 9)

    factorial(5)