# File: strings.py
# Description: Implements three functions that use
# and manipulate strings.
# Assignment Number: 9
#
# Name: Alicia Ireland
# EID:  ani324
# Email: alicianireland@gmaillcom
# Grader: Noah
#
#Â On my honor, Alicia Ireland, this programming assignment is my own work
#Â and I have not provided this code to any other student. 


# CS303e Students. Complete the 3 functions below.


# s1 and s2 shall be strings. This function returns the number of chars
# in s1 and s2 that match based on position.
def num_chars_same(s1, s2):
    count = 0
    shortest_string = s1 if len(s1) <= len(s2) else s2
    for i in range(0, len(shortest_string)):
        if s1[i] == s2[i]:
            count += 1
    return count


# s1 shall be a string and num shall be an integer >= 0.
# The function returns a stretched version of s1 with each
# character repeated. The number of repitions is num times
# the position of that character if we were to use 1 based indexing. 
def stretch(s1, num):
    new_string = ''
    for i in range(0, len(s1)):
        num_repeat = num*(i+1)
        new_string += num_repeat*s1[i]
    return new_string
     

# s1 and s2 shall be strings.
# The method returns the number of characters at the end of
# s1 and s2 that match. Stops at the first mistmatched character.
def length_of_matching_suffix(s1, s2):
    count = 0
    chr1, chr2 = '',''
    shortest_string = s1 if len(s1) <= len(s2) else s2
    for i in range(1, len(shortest_string)+1):
        chr1 += s1[-i]
        chr2 += s2[-i]
        if chr1 == chr2:
            count += 1
    return count
        

# Run tests on the functions. Ask the user for input.
def main():
    num_tests = eval(input('Enter the number of tests per method: '))
    print('Testing num chars same function.')
    test_functions_with_two_string_parameters(num_tests, num_chars_same)
    print('Testing stretch function.')
    stretch_tests(num_tests)
    print('Testing length of matching suffix function.')
    test_functions_with_two_string_parameters(num_tests,
                                              length_of_matching_suffix)


# Test the functions that take 2 String parameters.
def test_functions_with_two_string_parameters(num_tests, function_to_test):
    for i in range(0, num_tests):
        s1 = input('Enter first string: ')
        s2 = input('Enter second string: ')
        print(function_to_test(s1, s2))
    print()


# Test the stretch function.
def stretch_tests(num_tests):
    for i in range(0, num_tests):
        s1 = input('Enter the string: ')
        num = eval(input('Enter number of times to repeat: '))
        print(stretch(s1, num))
    print()
    

main()
