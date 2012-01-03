"""
/*
    The rules for writing Roman numerals allow for many ways of writing each number (see About Roman Numerals...). 
    However, there is always a "best" way of writing a particular number.

    For example, the following represent all of the legitimate ways of writing the number sixteen:

    IIIIIIIIIIIIIIII
    VIIIIIIIIIII
    VVIIIIII
    XIIIIII
    VVVI
    XVI

    The last example being considered the most efficient, as it uses the least number of numerals.

    The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers written in valid, 
    but not necessarily minimal, Roman numerals; that is, they are arranged in descending units and obey the subtractive pair 
    rule (see About Roman Numerals... for the definitive rules for this problem).

    Find the number of characters saved by writing each of these in their minimal form.

    Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.
*/


Rules:
1. Avoid more than 3 consecutive identical letters
2. Only I, X, and C can be used as the leading numeral in part of a subtractive pair.
   1. I can only be placed before V and X.
   2. X can only be placed before L and C.
   3. C can only be placed before D and M.

"""

import urllib

def minimize(roman):
    key  = ["DCCCC", "LXXXX", "VIIII", "IIII", "XXXX", "CCCC"]
    val  = ["CM"   , "XC"   , "IX"   , "IV"  , "XL"  , "CD"  ]
    mini = ""
    temp = roman
    for i in range(len(key)):
        roman =  roman.replace(key[i],val[i])
    mini = mini + roman
        
    return len(temp) - len(mini)
   

get = urllib.urlopen("https://raw.github.com/gist/1546542/50651c355a5b190868f03b3d6b44a1a84c15063e/ProjectEuler89.txt")
values = get.read().split('\n')


saved = sum([minimize(values[i]) for i in range(len(values))])

print saved

