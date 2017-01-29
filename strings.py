#!python

import string


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing"""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str)
    return is_palindrome_iterative(text)
    # return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    #mirrored strings test passed
    #non-palindromic tests passed
    #mixed casing test passed
    # letter_array = []
    # first = 0
    # last = len(text)-1
    # for letter in text:
    #     letter_array.append(letter.lower())
    # print letter_array
    letters = text.replace(" ", "").lower()
    first = 0
    last = len(text)-1
    letter_array = []
    while first<=last:
        if letter_array[first] == letter_array[last]:
            first = first + 1
            last = last - 1
        else:
            return False
    return True
    # first = 0
    # last = len(text)-1
    # while first<=last:
    #     if letter_array[first] == letter_array[last]:
    #         first = first + 1
    #         last = last - 1
    #     else:
    #         return False
    #
    # return True



def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here
    pass
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            str_not = 'a' if is_pal else 'not a'
            print('{}: {} is {} palindrome'.format(result, repr(arg), str_not))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
