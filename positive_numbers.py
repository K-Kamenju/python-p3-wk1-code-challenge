# Code begins here

# write a function, which takes three integers a, b, and c as arguments, and returns True if exactly two of of the three integers are positive numbers (greater than zero), and False - otherwise.

# We need to make use of an if elif statement

def two_positive_numbers(a, b, c):
    # the if and elif statement should return True if exactly two of the three integers are positive numbers (greater than zero)
    if a > 0 and b > 0 and c <= 0:
        return True
    elif a > 0 and b <= 0 and c > 0:
        return True
    elif a <= 0 and b > 0 and c > 0:
        return True
    # otherwise, the function should return False
    else:
        return False
    
# test cases - derived from the examples in the code challenge file

test_case_1 = two_positive_numbers(2, 4, -3)
test_case_2 = two_positive_numbers(-4, 6, 8)
test_case_3 = two_positive_numbers(4, -6, 9)
test_case_4 = two_positive_numbers(-4, 6, 0)
test_case_5 = two_positive_numbers(4, 6, 10)
test_case_6 = two_positive_numbers(-14, -3, -4)

# create a list of the test cases
tests = [test_case_1, test_case_2, test_case_3, test_case_4, test_case_5, test_case_6]

# print the list in the console to see if it matches the expected output
print(tests)
