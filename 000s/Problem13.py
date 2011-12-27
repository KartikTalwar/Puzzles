import urllib as get

data = get.urlopen("https://raw.github.com/gist/1522808/e3b3e9f6c95633296dd9bfeebfd435469b6eead4/ProjectEuler13.txt")
lines = data.read().split('\n')

sum = 0
for i in range(len(lines)):
	sum += int(lines[i])
	
print str(sum)[:10]
