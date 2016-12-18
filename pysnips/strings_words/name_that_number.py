import unittest

"""
Create a dictionary of the numbers and their names
create a list for the tens, such as 20, 30, 40, 50, 60...
if the number is between 0 and 19, get the dictionary value of that number
For numbers of 20 or larger, use divmod() to get both the number of tens and the remainder:

tens, below_ten = divmod(Number, 10)
Demo:

>>> divmod(42, 10)
(4, 2)

"""

NAMES = {0:"zero", 1: "one", 2: "two", 3: "three", 4: "four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine",
         10: "ten", 11: "eleven", 12: "twelve", 13:"thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18:"eighteen", 19: "nineteen"}
NAMES_TWO = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


def name_that_number(x):
    if x in range(0, 20):
        return NAMES.get(x)
    elif 20 <= x <= 99:
        tens, ones = divmod(x, 10)
        return NAMES_TWO[tens - 2] + " " + NAMES.get(ones) if ones != 0 else NAMES_TWO[tens-2]
    else:
        return "Number out of range"


class Tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(name_that_number(0), 'zero')

    def test2(self):
        self.assertEqual(name_that_number(4), 'four')

    def test3(self):
        self.assertEqual(name_that_number(9), 'nine')

    def test4(self):
        self.assertEqual(name_that_number(23), 'twenty three')

    def test5(self):
        self.assertEqual(name_that_number(20), "twenty")