def solution(s):
    swapped_string = ""

    for i in range(1, len(s), 2):
        swapped_string += s[i]
        swapped_string += s[i - 1]

    if len(swapped_string) != len(s):
        swapped_string += s[-1]

    return swapped_string
