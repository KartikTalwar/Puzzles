"""
/*
    If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

    If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

    NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
*/


// the words in the list can be replaced with their length as well

"""

def assembleCount():
	ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
	tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
	before = ones + ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
	tmp = []
	res = []
	
	for i in range(len(tens)):
		tmp.append(tens[i])
		for j in range(len(ones)):
			tmp.append(tens[i]+ones[j])
			
	first100 = before + tmp
	
	for i in range(len(ones)):
		res.append(ones[i]+"hundred")
		for j in range(len(first100)):
			res.append(ones[i]+"hundredand"+first100[j])
		
	final =  first100 + res + ["onethousand"]

	sum = 0
	for i in range(len(final)):
		sum += len(final[i])
	
	return sum


print assembleCount()


