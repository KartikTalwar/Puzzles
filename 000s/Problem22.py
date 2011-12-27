import urllib as get

data = get.urlopen("https://raw.github.com/gist/1523066/7b8986bf6ce94cb6e5b22e34ba9e809ae3ad8773/ProjectEuler22.txt")
parse = sorted(data.read().replace('"', '').split(','))


def worth(s):
	return sum([ord(s[i])-64 for i in range(len(s))])

total = sum([worth(parse[i])*(i+1) for i in range(len(parse))])

print total

