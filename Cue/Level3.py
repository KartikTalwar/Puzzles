"""
Level 3

----------------------------------------

Congratulations.  You have reached the final level.

For the final task, you must find all subsets of an array
where the largest number is the sum of the remaining numbers.
For example, for an input of:

(1, 2, 3, 4, 6)

the subsets would be

1 + 2 = 3
1 + 3 = 4
2 + 4 = 6
1 + 2 + 3 = 6

Here is the list of numbers you should run your code on.
The password is the number of subsets.  In the above case the
answer would be 4.
"""


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
