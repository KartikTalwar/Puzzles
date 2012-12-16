"""
/*
    You are given the following information, but you may prefer to do some research for yourself.

    - 1 Jan 1900 was a Monday.
    - Thirty days has September,
      April, June and November.
      All the rest have thirty-one,
      Saving February alone,
      Which has twenty-eight, rain or shine.
      And on leap years, twenty-nine.
    - A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

    How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
*/
"""


yr = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

def isLeap(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

sunday = 0
year = 1901
month = 1
leap = 0

import math
while year < 2001:
    for i in range(1,12):
        if isLeap(year):
            leap += 1
        sunday += math.floor(yr[month]/7)
    year += 1


print sunday + math.floor(leap/7)
