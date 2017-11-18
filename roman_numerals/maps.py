#!/usr/local/bin/python2.7
# encoding: utf-8

'''Maps for converting between Arabic and Roman numerals.'''


ANCIENT_NUMBER_MAP = ((10000, "ↂ"),
                      (5000, "ↁ"),
                      (1000, "M"),
                      (500, "D"),
                      (100, "C"),
                      (50, "L"),
                      (10, "X"),
                      (5, "V"),
                      (1, "I"))


MODERN_NUMBER_MAP = ((10000, "ↂ"),
                     (5000, "ↁ"),
                     (1000, "M"),
                     (900, "CM"),
                     (500, "D"),
                     (400, "CD"),
                     (100, "C"),
                     (90, "XC"),
                     (50, "L"),
                     (40, "XL"),
                     (10, "X"),
                     (9, "IX"),
                     (5, "V"),
                     (4, "IV"),
                     (1, "I"))
