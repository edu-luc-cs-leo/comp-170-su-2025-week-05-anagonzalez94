# Code

## Intersection of two strings
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
def is_alphabetical(string: str)-> bool:

## Letters only
def letters_only(string: str) -> str | None:

## Palindrome generator
def generate_palindrome(string: str) -> str | None:

## Palindrome detector
def is_palindrome(string: str) -> bool:
    
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
