# Code begins here

# You will have to define a function, which will be given an hour (always in the range of 1 to 12, inclusive), a minute (always in the range of 0 to 59, inclusive), and a period (either "am" or "pm") as input. Your task is to return a four-digit string that encodes that time in 24-hour time.

# Note for 24 hour systems in the am time, the time is the same just the format is different but for pm time, it is 12 but the stated time 

# We need to make use of an if elif statement

def convert_12hr_to_24hr(hour, minute, period):
    # this converts the 12-hour time to 24-hour time based on the period
    if period == "pm" and hour < 12:
        hour = hour + 12
    elif period == "am" and hour == 12:
        hour = 0
    # this converts the hour/minute to a string and adds a leading zero if necessary.
    # note the :02d format specifier is used to ensure that the hour and minute are always two digits with a leading zero if necessary
    converted_hour = f"{hour:02d}"
    converted_minute = f"{minute:02d}"
    # this combines the hour and minute into a string
    converted_time = converted_hour + converted_minute
    return converted_time

# test cases - derived from the examples in the code challenge file

test_case_1 = convert_12hr_to_24hr(8, 30, "am")
test_case_2 = convert_12hr_to_24hr(8, 30, "pm")
test_case_3 = convert_12hr_to_24hr(12, 00, "pm")
test_case_4 = convert_12hr_to_24hr(12, 00, "am")
test_case_5 = convert_12hr_to_24hr(12, 15, "am")
test_case_6 = convert_12hr_to_24hr(12, 15, "pm")

# create a list of the test cases
tests = [test_case_1, test_case_2, test_case_3, test_case_4, test_case_5, test_case_6]

# print the list in the console to see if it matches the expected output
print(tests)