# Python Week 1 - Code Challenge

The code challenge involves coming up with solutions to three challenges that will be described below.

## Project Setup

1. Create a new project folder.
2. Create a new GitHub repository
3. Please make sure you regularly commit to the repository.
4. Ensure to add a READEME.md file
5. Add a License file, preferrably the MIT license
6. Ensure to organize your python solution in a lib folder

## `Challenge 1: 12-hour to 24-hour Time Conversion`

This code provides a solution to the challenge of converting a 12-hour time format to a 24-hour time format. The function takes an hour (in the range of 1 to 12, inclusive), a minute (in the range of 0 to 59, inclusive), and a period ("am" or "pm") as input and returns a four-digit string representing the time in 24-hour format.

### Function Description

The function convert_12hr_to_24hr(hour, minute, period) converts a 12-hour time to a 24-hour time based on the given input parameters. It handles cases such as converting "pm" times to the equivalent on the 24-hour clock. Additionally, it ensures that the output string always includes two digits for both hours and minutes.

### Implementation

The implementation utilizes an if and elif statement to handle the conversion logic:

```python

def convert_12hr_to_24hr(hour, minute, period):
    # Convert the 12-hour time to 24-hour time based on the period
    if period == "pm" and hour < 12:
        hour = hour + 12
    elif period == "am" and hour == 12:
        hour = 0
    # Convert the hour/minute to a string and add a leading zero if necessary
    converted_hour = f"{hour:02d}"
    converted_minute = f"{minute:02d}"
    # Combine the hour and minute into a string
    converted_time = converted_hour + converted_minute
    return converted_time

```

### Test Cases

Test cases have been created based on the examples provided in the code challenge. The results of these test cases are stored in a list named tests. Each test case checks the function against specific input values.

```python

# Test cases derived from the examples in the code challenge file
test_case_1 = convert_12hr_to_24hr(8, 30, "am")
test_case_2 = convert_12hr_to_24hr(8, 30, "pm")
test_case_3 = convert_12hr_to_24hr(12, 00, "pm")
test_case_4 = convert_12hr_to_24hr(12, 00, "am")
test_case_5 = convert_12hr_to_24hr(12, 15, "am")
test_case_6 = convert_12hr_to_24hr(12, 15, "pm")

# Create a list of the test cases
tests = [test_case_1, test_case_2, test_case_3, test_case_4, test_case_5, test_case_6]

# Print the list to the console to verify the results
print(tests)

```

## `Challenge 2: Two numbers are positive`

This code provides a solution to the challenge of determining whether exactly two out of three given integers are positive numbers.

### Function Description

The function two_positive_numbers(a, b, c) takes three integers a, b, and c as arguments and returns True if exactly two of the three integers are positive numbers (greater than zero), and False otherwise.

### Implementation

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

### Test Cases

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

## `Challenge 3: Consonant value`

This code provides a solution to the challenge of finding the highest value of consonant substrings in a given lowercase string. Consonants are defined as any letters of the alphabet except "aeiou", and their values are assigned as follows: a = 1, b = 2, c = 3, ..., z = 26.

### Function Description

The function consonant_value_calculation(word) takes a lowercase string containing alphabetic characters only (no spaces) as input. It returns the highest value among the consonant substrings in the given string.

### Implementation

The implementation involves a nested function string_value(string) that converts a string of characters into their numeric values using the ord() function. The main function iterates through the lowercase input string, identifies consonants, and calculates the values of consonant substrings.

```python

def consonant_value_calculation(word):
    # Nested function to convert string characters to numeric values
    def string_value(string):
        return sum(ord(i) - 96 for i in string)

    # Convert the word to lowercase
    word_lower_case = word.lower()

    # Initialize empty lists and strings
    consonant_value = []
    current_substring = ''

    # Iterate through the string
    for letter in word_lower_case:
        # If the letter is not a vowel, add it to the current substring
        if letter not in 'aeiou':
            current_substring = current_substring + letter
        else:
            # If the letter is a vowel, add the value of the current substring to the consonant value list
            if current_substring:
                consonant_value.append(string_value(current_substring))
                current_substring = ''

    # Add the value of the last substring to the consonant value list
    if current_substring:
        consonant_value.append(string_value(current_substring))

    # Return the maximum consonant value
    return max(consonant_value)

```

### Test Cases

Test cases have been created based on the examples provided in the code challenge. I have also added tests that will capture the data if an uppercase string is inputed. The results of these test cases are stored in a list named tests. Each test case checks the function against specific input values.

```python

# Test cases derived from the examples in the code challenge file
test_case_1 = consonant_value_calculation("zodiacs")
test_case_2 = consonant_value_calculation("strength")
test_case_3 = consonant_value_calculation("ZODIACS")
test_case_4 = consonant_value_calculation("STRENGTH")

# Create a list of the test cases
tests = [test_case_1, test_case_2, test_case_3, test_case_4]

# Print the list to the console to verify the results
print(tests)

```