"""
/*

    Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

*/
"""

import urllib as get

data = get.urlopen("https://raw.github.com/gist/1522808/e3b3e9f6c95633296dd9bfeebfd435469b6eead4/ProjectEuler13.txt")
lines = data.read().split('\n')

sum = 0
for i in range(len(lines)):
	sum += int(lines[i])
	
print str(sum)[:10]
