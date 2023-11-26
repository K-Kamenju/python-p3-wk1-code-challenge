# code begins here

# Given a lowercase string that has alphabetic characters only and no spaces, return the highest value of consonant substrings. Consonants are any letters of the alphabet except "aeiou".We shall assign the following values: a = 1, b = 2, c = 3, .... z = 26.

def consonant_value_calculation(word):
    # This is a nested function that allows us to convert the string characters into their number values through the ord() function
    def string_value(string):
        return sum(ord(i) - 96 for i in string)
    
    # convert the word to lowercase
    word_lower_case = word.lower()

    # iniate an empty list to store the consonant values
    consonant_value = []
    # initiate an empty string to store the current substring
    current_substring = ''

    # iterate through the string
    for letter in word_lower_case:
        # if the letter is not a vowel, add it to the current substring
        if letter not in 'aeiou':
            current_substring = current_substring + letter
        else:
            # if the letter is a vowel, add the value of the current substring to the consonant value list
            if current_substring:
                consonant_value.append(string_value(current_substring))
                current_substring = ''

    # add the value of the last substring to the consonant value list
    if current_substring:
        consonant_value.append(string_value(current_substring))

    # return the maximum consonant value
    return max(consonant_value)

# test cases - derived from the examples in the code challenge file

test_case_1 = consonant_value_calculation("zodiacs")
test_case_2 = consonant_value_calculation("strength")
test_case_3 = consonant_value_calculation("ZODIACS")
test_case_4 = consonant_value_calculation("STRENGTH")

# create a list of the test cases
tests = [test_case_1, test_case_2, test_case_3, test_case_4]

# print the list in the console to see if it matches the expected output
print(tests)