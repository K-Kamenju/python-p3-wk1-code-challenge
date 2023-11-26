## Challenge 2: Two numbers are positive

This code provides a solution to the challenge of determining whether exactly two out of three given integers are positive numbers.

### Function Description

The function two_positive_numbers(a, b, c) takes three integers a, b, and c as arguments and returns True if exactly two of the three integers are positive numbers (greater than zero), and False otherwise.

### `Implementation`

The implementation utilizes an if and elif statement to check the conditions for exactly two positive numbers:

```python

def two_positive_numbers(a, b, c):
    # Check if exactly two out of the three integers are positive
    if a > 0 and b > 0 and c <= 0:
        return True
    elif a > 0 and b <= 0 and c > 0:
        return True
    elif a <= 0 and b > 0 and c > 0:
        return True
    # If none of the conditions are met, return False
    else:
        return False

```

### `Test Cases`

Test cases have been created based on the examples provided in the code challenge. The results of these test cases are stored in a list named tests. Each test case checks the function against specific input values.

```python

# Test cases derived from the examples in the code challenge file
test_case_1 = two_positive_numbers(2, 4, -3)
test_case_2 = two_positive_numbers(-4, 6, 8)
test_case_3 = two_positive_numbers(4, -6, 9)
test_case_4 = two_positive_numbers(-4, 6, 0)
test_case_5 = two_positive_numbers(4, 6, 10)
test_case_6 = two_positive_numbers(-14, -3, -4)

# Create a list of the test cases
tests = [test_case_1, test_case_2, test_case_3, test_case_4, test_case_5, test_case_6]

# Print the list to the console to verify the results
print(tests)

```