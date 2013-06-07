import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    if int(test) % 2 is 0:
        print 1
    else:
        print 0

test_cases.close()
