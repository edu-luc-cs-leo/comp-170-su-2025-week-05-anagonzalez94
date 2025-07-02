# Code

## Intersection of two strings
"""
Finds and returns characters in common between two given strings with no duplicates.

Parameters:
    foo (str): a string
    bar (str): a string

Returns:
    str or None: The characters in common between the strings, or None if the string is empty/None.
"""
def intersection(foo: str, bar: str) -> str | None:
    # Empty string to add our resulting characters into
    common_ch = ""
    # Check if characters in first string appear in the second string
    for ch in foo:
        if ch in bar and not ch in common_ch: # Make sure there are no duplicate characters
            # Concatenate characters found to be in common to the empty string
            common_ch += ch
    return common_ch

## Alphabetical assessment
"""
Determines if all of the characters in a given string are alphabetical

Parameters:
    string (str): a string

Returns:
    bool: True if every character is alphabetical, False if the string contains numbers or special characters
"""
def is_alphabetical(string: str) -> bool:
    alpha_check = False
    if string is not None and len(string) > 0 and string.isalpha(): # I got a little stuck here, and used outside resources after exhausting my own attempts.
        alpha_check = True
    return alpha_check

## Letters only
"""
Finds and returns only the alphabetical characters in a given string.

Parameters:
    string (str): a string

Returns:
    str or None: The alphabetical characters, or None if the string is empty/None.
"""
def letters_only(string: str) -> str | None:
    letters = None
    if string is not None and len(string) > 0:
        letters = ""
        for i in range(len(string)):
            # Find ASCII value of each character, referenced in-class coding JUN23
            current_ch = string[i]
            current_ascii = ord(current_ch)
            # Determine if the ASCII of each character is alphabetical
            if current_ascii >= ord('a') and current_ascii <= ord('z') or current_ascii >= ord('A') and current_ascii <= ord('Z'):
                valid_ch = chr(current_ascii)
            else:
                # Gets rid of non-alphabetical characters
                valid_ch = ""
            # Concatenate alphabetical characters to empty string
            letters = letters + valid_ch
    return letters

## Palindrome generator
"""
Generates a palindrome given a string

Parameters: 
    string (str): a string

Returns:
    str or None: A palindrome or None if the string is empty/None
"""
def generate_palindrome(string: str) -> str | None:
    palindrome = None
    if string is not None and len(string) > 0:
        # Determine if the length of the given string is odd or even
        if len(string) % 2 != 0:
            # Slice string to remove last character and reverse
            palindrome = string + string[:-1][::-1] # Concatenate sliced string with original string
        else:
            # Slice string to reverse ONLY
            palindrome = string + string[::-1] 
    return palindrome

## Palindrome detector
"""
Determines whether or not a string is a palindrome (the same forwards and backwards)

Parameters:
    string (str): a string

Returns:
    bool: True if the string is a palindrome, False if not
"""
def is_palindrome(string: str) -> bool:
    palin_check = ""
    if string is not None and len(string) > 0:
        # Only examine alphabetical characters in order to determine palindrome
        for i in range(len(string)):
            current_ch = string[i]
            current_ascii = ord(current_ch)
            if current_ascii >= ord('A') and current_ascii <= ord('Z'):
                new_ascii = current_ascii + 32 # Makes all uppercase characters into lowercase
                palin_check += chr(new_ascii) # Concatenates characters into empty string
            elif current_ascii >= ord('a') and current_ascii <= ord('z'):
                palin_check += current_ch
    # In order to not receive "True" on and empty string, specify length of test string
    return len(palin_check)>0 and palin_check == palin_check [::-1]




#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 
print(''.join([
    chr(10), chr(10),
    chr(87), chr(104), chr(101), chr(110), chr(32),
    chr(121), chr(111), chr(117), chr(32), chr(97), chr(114), chr(101), chr(32),
    chr(114), chr(101), chr(97), chr(100), chr(121), chr(32), chr(116), chr(111), chr(32),
    chr(116), chr(101), chr(115), chr(116), chr(32), chr(121), chr(111), chr(117), chr(114), chr(32),
    chr(99), chr(111), chr(100), chr(101), chr(44), chr(32),
    chr(99), chr(111), chr(110), chr(116), chr(97), chr(99), chr(116), chr(32),
    chr(76), chr(101), chr(111), chr(32), chr(102), chr(111), chr(114), chr(32),
    chr(116), chr(104), chr(101), chr(32), chr(116), chr(101), chr(115), chr(116), chr(32),
    chr(109), chr(101), chr(116), chr(104), chr(111), chr(100), chr(46), chr(10), chr(10)
]))
#
# Testing here is done a bit more formally than using simple print statements.
# This type of testing is called "Unit Testing" and can be extremely useful.
# Unit testing applies to small components of the software we write -- in this
# case the units tested are the individual methods we wrote.
#

import unittest


class TestStringMethods(unittest.TestCase):

    def test_intersection(self):
        self.assertEqual(intersection("airplanes", "repairman"), "airpne")
        self.assertEqual(intersection("abc", "def"), "")
        self.assertEqual(intersection("hello", "hello"), "hello")
        self.assertEqual(intersection("aaaa", "aaa"), "a")
        self.assertEqual(intersection("", "abc"), None)
        self.assertEqual(intersection("abc", ""), None)
        self.assertEqual(intersection("", ""), None)
        self.assertEqual(intersection("abc", "cab"), "abc") # preserves order of `foo`

    def test_is_alphabetical(self):
        self.assertTrue(is_alphabetical("abcXYZ"))
        self.assertFalse(is_alphabetical("abc1"))
        self.assertFalse(is_alphabetical("hello!"))
        self.assertFalse(is_alphabetical(" "))
        self.assertFalse(is_alphabetical(""))
        self.assertFalse(is_alphabetical(None))
        self.assertTrue(is_alphabetical("ZzAaBb"))

    def test_letters_only(self):
        self.assertEqual(letters_only("abc123XYZ!@#"), "abcXYZ")
        self.assertEqual(letters_only("!@#$%^&*()"), "")
        self.assertEqual(letters_only(""), None)
        self.assertEqual(letters_only(None), None)
        self.assertEqual(letters_only("LettersONLY"), "LettersONLY")

    def test_generate_palindrome(self):
        self.assertEqual(generate_palindrome("mice"), "miceecim")
        self.assertEqual(generate_palindrome("mad"), "madam")
        self.assertEqual(generate_palindrome("a"), "a")
        self.assertEqual(generate_palindrome(""), None)
        self.assertEqual(generate_palindrome(None), None)

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("Racecar"))
        self.assertTrue(is_palindrome("A man, a plan, a canal, Panama"))
        self.assertTrue(is_palindrome("No 'x' in Nixon"))
        self.assertFalse(is_palindrome("Hello"))
        self.assertFalse(is_palindrome("Palindrome"))
        self.assertFalse(is_palindrome(""))
        self.assertFalse(is_palindrome(None))


# This allows the test to be run from the command line using `python -m unittest filename.py`
if __name__ == '__main__':
    unittest.main()