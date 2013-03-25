
def countSubsets(numbers):
    numbers = sorted(numbers)
    array   = {0 : 1}
    answer  = 0

    for number in numbers:
        if number in array:
            answer += array[number]

        last = [(i, j) for (i, j) in array.iteritems()]

        for (s, c) in last:
            array.setdefault(s + number, 0)
            array[s + number] += c

    return answer


numbers = [3, 4, 9, 14, 15, 19, 28, 37, 47, 50, 54, 56, 59, 61, 70, 73, 78, 81, 92, 95, 97, 99]

print countSubsets(numbers)
