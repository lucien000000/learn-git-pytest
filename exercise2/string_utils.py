# Exercise 2: String Utilities


def reverse_string(s: str) -> str:
    """
    Return the input string in reverse order.

    Args:
        s: Input string

    Returns:
        The reversed string
    """
    l = ""
    for elt in s:
        l = elt + l
    return l


def count_vowels(s: str) -> int:
    """
    Return the number of vowels (a, e, i, o, u) in the input string.
    Case-insensitive: both uppercase and lowercase vowels should be counted.

    Args:
        s: Input string

    Returns:
        The number of vowels in the string
    """
    s.lower()
    i = 0
    L=[a,e,i,o,u]
    for elt in s:
        if elt in L:
            i += 1
    return i

import math

def is_palindrome(s: str) -> bool:
    """
    Check if the input string is a palindrome.
    A palindrome reads the same backward as forward.
    Spaces and case should be ignored.

    Args:
        s: Input string

    Returns:
        True if the string is a palindrome, False otherwise
    """
    n = len(s)
    A1 = s[:math.floor(n/2)]
    A2 = s[math.ceil(n/2):]
    if A1 == A2[::-1]:
        return True
    


def capitalize_words(s: str) -> str:
    """
    Capitalize the first letter of each word in the input string.

    Args:
        s: Input string

    Returns:
        The input string with the first letter of each word capitalized
    """
    s[0].upper()
    for i in range(len(s)):
        if s[i] == " ":
            s[i+1].upper()
    return s
